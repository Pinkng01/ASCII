from typing import List
import os
import time
import keyboard
import math


class Vertex:
    def __init__(this ,depth: str):
        this.alpha:str = depth
        pass
    def __str__(this):
        return this.alpha

def renderScreenList(ScrList: List[str]):
    for i in range(len(ScrList)):
        print("")
        for k in range(len(ScrList[i])):
            print(str(ScrList[i][k].alpha), end="")
        
height: int = 40
widnth: int = 120
amplitude: float = height / 2.0 - 1 
freq: float = 2.0

scrList = [[Vertex(" ") for i in range(widnth)] for k in range(height)]
#for x in range(0, widnth, 1):
x: int = 0
while(True):
    x +=1
    if( x == 120):
        x= 0
        scrList = [[Vertex(" ") for i in range(widnth)] for k in range(height)]
#for x in range(0, widnth, 1):
    angle: float = freq * (2.0 * math.pi * x/widnth)
    y: float = int(amplitude * ( 1 + math.cos(angle)))
    y1: float = int(amplitude * ( 1 + math.sin(angle)))
    scrList[y][x].alpha = '='
    scrList[y1][x].alpha = '='
    renderScreenList(scrList)
    time.sleep(0.1)
    os.system('cls')
    try:
        if(keyboard.is_pressed('q')):
           break
    except:
        continue
