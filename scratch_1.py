from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *


class Coordinates():
    replayButton=(400,425)
    dino=(177,405)#427

def restartGame():
    pyautogui.click(Coordinates.replayButton)


def jump():
    pyautogui.keyDown('space')
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box=(Coordinates.dino[0]+60,Coordinates.dino[1],Coordinates.dino[0]+105,Coordinates.dino[1]+30 )
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

def main():
    restartGame()
    while True:
        if(imageGrab()!=1597):
            jump()
            time.sleep(0.1)
main()