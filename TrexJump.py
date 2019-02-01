#Importing Required Packages

from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

#Use Paint.Net to get pixel coordinates

class Coordinates():
    replayButton=(400,425)  #coordinates of replay button 
    dino=(177,405)  #x coordinates of top right corner of the T-rex
                    #y coordinates to take in lowest obstacle   

#Function to restart game

def restartGame():
    pyautogui.click(Coordinates.replayButton)

#Function to make the dinosaur jump

def jump():
    pyautogui.keyDown('space')
    print("Jump")
    pyautogui.keyUp('space')

#Function to return grayscale sum of pixels ahead of the dino to check for trees and birds

def imageGrab():
    box=(Coordinates.dino[0]+60,Coordinates.dino[1],Coordinates.dino[0]+105,Coordinates.dino[1]+30 )
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

#Function restarts the game and dino jumps whenever there is an obstacle infront of it

def main():
    restartGame()
    while True:
        if(imageGrab()!=1597):  #1597 is the sum when there is no obstacle in front of dino
            jump()
            time.sleep(0.1)
main()
