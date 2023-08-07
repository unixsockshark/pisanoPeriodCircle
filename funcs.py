import pygame

import math

lastHighestNum = 0
 



nodes = []
def drawNode(x,y,name, surf):
    global lastHighestNum
    pygame.draw.circle(surf, (0,0,0), (x,y), 25, 25)
    if  lastHighestNum < name + 1: 
        newtab = {"name":name, "pos":(x,y)} 
        nodes.append(newtab)
        lastHighestNum = name + 1
def calculateNodes(num, surf):
    center_x = 1280 // 2
    center_y = 720 // 2
    radius = 250
    
    for i in range(num):
        radianIncrement = 2 * math.pi / num



        nodeRadians = math.pi - radianIncrement * i  # Start at 1 pi radian
        x = center_x + radius * math.cos(nodeRadians)
        y = center_y - radius * math.sin(nodeRadians)
        drawNode(x, y, i, surf)

