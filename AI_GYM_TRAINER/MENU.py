import cv2
import numpy as np
import time
import PoseModule as pm

path = "K:\PROJECT\AI_GYM_TRAINER\VIDEOS"

def DPU():
    print("DPU")
def IPU():
    print("IPU")
def DC():
    print("DC")
def DR():
    print("DR")
def GB():
    print("GB")
def GP():
    print("GP")
def HC():
    print("HC")
def P():
    print("P")
def PU():
    print("PU")
def SSPU():
    print("SSPU")
def TBR():
    print("TBR")
def TPD():
    print("TPD")

details = {1:["Decline Push Up", DPU], 2: ["Incline Push Up", IPU], 3:["Dumbell Curls", DC], 4:["Dumbell Row", DR], 5:["Glute Bridge", GB],6:["Ground Pully", GP],
           7:["Hammer Curl", HC], 8: ["Plank", P], 9:["Pushup",PU], 10:["Side Shoulder Push Up", SSPU], 11:["T Bar Row", TBR], 12:["Tricep Push Down", TPD]}

while True:
    print("---------------Menu---------------")
    for a in details:
        print(a, ":", details[a][0])
    print("----------------------------------")
    
    choice = int(input("Enter your choice: "))
    if(choice in details.keys()):
        details[choice][1]()
        
    