import PIL
from matplotlib.patches import Rectangle
import pyautogui
import pydirectinput
import time
import numpy as np
import keyboard
import cv2 as cv
from matplotlib import pyplot as plt
import scipy

'screenbox= (555,250,1395,735)'
'(region=(555,250,840,485))'

'health bar ranges'
healthmin = np.array([47,47,211])
healthmax = np.array([47,47,211])

'mouse movement'
x=100
y=100

'GUI positions' 
hunger = (990,920,1230,950)
health = (898,658,960,675)
slot1 = (699,982,743,1029)
slot2 = (759,982,803,1029)
slot3 = (819,982,863,1029)
slot4 = (879,982,924,1029)
slot5 = (939,982,983,1029)
slot6 = (999,982,1043,1029)
slot7 = (1059,982,1103,1029)
slot8 = (1119,982,1163,1029)
slot9 = (1179,982,1223,1029)

found_block = False
commands = True

def wdown():
    pydirectinput.keyDown('w')
def adown():
    pydirectinput.keyDown('a')
def sdown():
    pydirectinput.keyDown('s')
def ddown():
    pydirectinput.keyDown('d')
def rightdown():
    pydirectinput.mouseDown
def rightclick():
    pydirectinput.rightClick
def leftclick():
    pydirectinput.leftClick
def movemouse():
    pydirectinput.moveRel(x,y)

def movement():
    while commands:
        wdown()


def pictures():
    img = pyautogui.screenshot(region=(555,250,840,485))
    "img.save('D:\Coding\Minecwaft bot\Screenshots\currentimg.png', format='png')"
    "img = cv.imread('D:\Coding\Minecwaft bot\Screenshots\currentimg.png',1)"
    img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    blurred = cv.GaussianBlur(img, (11, 11),0)
    rgb = cv.cvtColor(cv.UMat(img), cv.COLOR_BGR2RGB)
    edged = cv.Canny(blurred,30,90)
    losshrt(img)
    'cv.imshow("image", blurred)'
    cv.waitKey(16)
    return img
    
'health red range 200-220 brightness'
'found how much health you have'
def losshrt(img): 
    redpxl = img[409:424, 244:406]
    hrts = cv.inRange(redpxl, healthmin, healthmax)
    nored = int(cv.countNonZero(hrts)/226)
    print("you have " + str(nored) + " hearts")
    'cv.rectangle(img,(245,405), (405,425), (0,0,255),2 )'
    cv.imshow('red rectangle',redpxl)
    cv.waitKey(16)

while not found_block:
   'wdown()'
   img=pictures()
   losshrt(img)

def found_block():
    pydirectinput.keyUp("w")