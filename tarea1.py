# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:14:53 2018

@author: Rodrigo
"""
import os
import sys
import numpy as np
import cv2
from auxiliar.disjointUnionSets import disjointUnionSets
import auxiliar.contourTracing as contourTracing
import auxiliar.circle as circle

class tarea1:

    def main(rgb_image):
        #creamos los directorios donde guardaremos los outputs si es que no existen
        if not os.path.exists('binaryImages/'):
            os.makedirs('binaryImages/')
        if not os.path.exists('detectedCircles/'):
            os.makedirs('detectedCircles/')
        if not os.path.exists('outputData/'):
            os.makedirs('outputData/')
        original = str(rgb_image)
        #leemos la imagen RGB
        img = cv2.imread(original)
        #creamos una copia con la que trabajaremos
        yellow = img.copy()
        h = yellow.shape[0]
        w = yellow.shape[1]
        #resaltamos los colores amarillos para que sean perfectos amarillos
        for i in range(h):
            for j in range(w):
                if (yellow[i, j, 0] < 45) and (yellow[i, j, 1] > 90) and (yellow[i, j, 2] > 120):
                    yellow[i, j, 0] = 0 #canal azul
                    yellow[i, j, 1] = 255 #canal verde
                    yellow[i, j, 2] = 255 #canal rojo
        
        #creamos una imagen en tonos de grises
        gray = cv2.cvtColor(yellow, cv2.COLOR_BGR2GRAY)
        #aplicamos un threshold detectado a prueba y error para crear la imagen binaria
        ret, binarized = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
        #guardamos la imagen binaria
        cv2.imwrite( "binaryImages/Binary_Image_" + original, binarized)
        #aplicamos el threshold nuevamente para guardar los pixeles blancos con un 1
        ret, binarized = cv2.threshold(gray, 220, 1, cv2.THRESH_BINARY)
        
        #buscamos las componentes conexas, los puntos de cada componente y los datos para
        #generar las bounding boxes
        components, lpoints, squares = disjointUnionSets.countConnectedComponents(binarized)
        finalPoints = [[] for _ in range(components)]
        
        pointsMatrix = (np.reshape(np.asarray(lpoints), (-1,3))).astype(int)
        for i in range(len(pointsMatrix)):
            finalPoints[pointsMatrix[i][2]-1].append(pointsMatrix[i,:2].tolist())
        n = len(binarized)
        m = len(binarized[0])
        lista = binarized.flatten().tolist()
        #encontramos los contornos de las componentes conexas
        borders = contourTracing.contourTracing(lista, m, n)
        arr = np.reshape(np.asarray(borders), (n,m)).astype(np.uint8, copy=False)
        components2, lpoints2, squares2 = disjointUnionSets.countConnectedComponents(arr)
        finalBorders = [[] for _ in range(components2)]
        
        bordersMatrix = (np.reshape(np.asarray(lpoints2), (-1,3))).astype(int)
        for i in range(len(bordersMatrix)):
            finalBorders[bordersMatrix[i][2]-1].append(bordersMatrix[i,:2].tolist())
        
        #analizamos los bordes para detectar cuales son circulos
        realCircles = {}
        for i in range(components):
            if (abs(squares[i+1][2] - squares[i+1][3]) > 5):
                continue
            l = circle.pick3RandomPoints(finalBorders[i])
            circ = circle.createCircle(l[0],l[1],l[2])
            radioReal = np.mean([squares[i+1][2],squares[i+1][3]]) / 2
            if (circle.isCircular(circ,radioReal,0.25)):
                realCircles[i+1] = squares[i+1]
        
        #generamos las imagenes con bounding boxes en las componentes circulares
        for key in realCircles:
            cv2.rectangle(img,(realCircles[key][1],realCircles[key][0]),(realCircles[key][1]+realCircles[key][3],realCircles[key][0]+realCircles[key][2]),(0,255,0),2)
        cv2.imwrite( "detectedCircles/Detected_Image_" + original, img)
        a,b = original.split('.')
        f = open('outputData/' + a + '.txt','w')
        f.write("La imagen tiene " + str(components) + " componentes conexas \n")
        f.write("Los siguientes elementos son los puntos de cada componente conexa y la componente a la que pertenecen (x,y,id):\n")
        for item in pointsMatrix:
            f.write("%s\n" % item)
        f.write("Los siguientes elementos son los puntos de cada borde de cada componente conexa y la componente a la que pertenecen (x,y,id):\n")
        for item in bordersMatrix:
            f.write("%s\n" % item)
        f.write("Los siguientes elementos son los puntos x e y que representan el punto inicial del rectangulo minimo que cubre a cada componente, con un ancho w y alto h (x,y,w,h):\n")
        for item in squares:
            f.write(str(item) + "" + str(squares.get(item)) + "\n")
        f.close()
        
    if __name__ == "__main__":
        main(sys.argv[1])
