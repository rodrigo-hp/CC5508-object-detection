# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 13:32:34 2018

@author: Rodrigo
"""

class disjointUnionSets:
    
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [0] * n
        self.n = n
        for i in range(n):
            self.parent[i] = i
    
    def find(self, x):
        if (self.parent[x] != x):
            return self.find(self.parent[x])
        return x
    
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        
        if (xRoot == yRoot):
            return
        
        if (self.rank[xRoot] < self.rank[yRoot]):
            self.parent[xRoot] = yRoot
        
        elif (self.rank[yRoot] < self.rank[xRoot]):
            self.parent[yRoot] = xRoot
            
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] = self.rank[xRoot] + 1
            
    def countConnectedComponents(binarized):
        
        n = len(binarized)
        m = len(binarized[0])
        dus = disjointUnionSets(n*m)
        
        for j in range(n):
            for k in range(m):
                if (binarized[j][k] == 0):
                    continue
        
                if (j+1 < n and binarized[j+1][k] == 1):
                    dus.union(j*(m)+k, (j+1)*(m)+k)
                if (j-1 >= 0 and binarized[j-1][k]==1):
                    dus.union(j*(m)+k, (j-1)*(m)+k)
                if (k+1 < m and binarized[j][k+1]==1):
                    dus.union(j*(m)+k, (j)*(m)+k+1)
                if (k-1 >= 0 and binarized[j][k-1]==1):
                    dus.union(j*(m)+k, (j)*(m)+k-1)
                if (j+1<n and k+1<m and binarized[j+1][k+1]==1):
                    dus.union(j*(m)+k, (j+1)*(m)+k+1)
                if (j+1<n and k-1>=0 and binarized[j+1][k-1]==1):
                    dus.union(j*m+k, (j+1)*(m)+k-1)
                if (j-1>=0 and k+1<m and binarized[j-1][k+1]==1):
                    dus.union(j*m+k, (j-1)*m+k+1)
                if (j-1>=0 and k-1>=0 and binarized[j-1][k-1]==1):
                    dus.union(j*m+k, (j-1)*m+k-1)
            
        c = [0] * n * m
        numberOfContours = 0
        lpoints = []
        dual = {}
        squares = {}
        for j in range(n):
            for k in range(m):
                if (binarized[j][k] == 1):
                    x = dus.find(j*m + k)
                    
                    if (c[x] == 0):
                        numberOfContours += 1
                        c[x] += 1
                        lpoints.append([j,k,x])
                        dual[x] = numberOfContours
                        squares[numberOfContours] = [j,k,0,0]
                    else:
                        c[x] += 1
                        lpoints.append([j,k,x])
                        if (j < squares[dual[x]][0]):
                            squares[dual[x]][0] = j
                        elif (j > squares[dual[x]][2]):
                            squares[dual[x]][2] = j
                        elif (k < squares[dual[x]][1]):
                            squares[dual[x]][1] = k
                        elif (k > squares[dual[x]][3]):
                            squares[dual[x]][3] = k
                            
        for i in range(1,len(squares)+1):
            squares[i][2] = squares[i][2] - squares[i][0]
            squares[i][3] = squares[i][3] - squares[i][1]
            
        for i in range(len(lpoints)):
            lpoints[i][2] = dual.get(lpoints[i][2])
            
        return numberOfContours, lpoints, squares