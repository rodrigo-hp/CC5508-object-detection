# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 04:37:09 2018

@author: Rodrigo
"""


def padImage(image, width, height, paddingColor):
    paddedImage = [0] * (height + 2) * (width + 2)
    for x in range(width + 2):
        for y in range(height + 2):
            if (x == 0) or (y == 0) or (x == width + 1) or (y == height + 1):
                paddedImage[x + y * (width + 2)] = paddingColor
            else:
                paddedImage[x + y * (width + 2)] = image[x - 1 + (y - 1) * width]

    return paddedImage


def contourTracing(image, width, height):
    inside = False
    pos = 0

    paddedImage = padImage(image, width, height, 1)
    borderImage = [0] * (height + 2) * (width + 2)
    for y in range(height + 2):
        for x in range(width + 2):
            borderImage[x + y * (width + 2)] = 0

    for y in range(height + 2):
        for x in range(width + 2):
            pos = x + y * (width + 2)
            if (borderImage[pos] == 1 and not (inside)):
                inside = True
            elif (paddedImage[pos] == 1 and inside):
                continue
            elif (paddedImage[pos] == 0 and inside):
                inside = False
            elif (paddedImage[pos] == 1 and not (inside)):
                borderImage[pos] = 1
                checkLocationNr = 1
                startPos = pos
                counter = 0
                counter2 = 0

                neighborhood = [
                    [-1, 7],
                    [-3 - width, 7],
                    [-width - 2, 1],
                    [-1 - width, 1],
                    [1, 3],
                    [3 + width, 3],
                    [width + 2, 5],
                    [1 + width, 5]
                ]
                while (True):
                    checkPosition = pos + neighborhood[checkLocationNr - 1][0]
                    newCheckLocationNr = neighborhood[checkLocationNr - 1][1]

                    if (paddedImage[checkPosition] == 1):
                        if (checkPosition == startPos):
                            counter += 1

                            if (newCheckLocationNr == 1 or counter >= 3):
                                inside = True
                                break

                        checkLocationNr = newCheckLocationNr
                        pos = checkPosition
                        counter2 = 0
                        borderImage[checkPosition] = 1
                    else:
                        checkLocationNr = 1 + (checkLocationNr % 8)
                        if (counter2 > 8):
                            counter2 = 0
                            break
                        else:
                            counter2 += 1

    clippedBorderImage = [0] * (height) * (width)
    for x in range(width):
        for y in range(height):
            clippedBorderImage[x + y * width] = borderImage[x + 1 + (y + 1) * (width + 2)]

    return clippedBorderImage
