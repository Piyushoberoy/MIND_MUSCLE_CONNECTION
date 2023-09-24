import cv2
import numpy as np
import time
import PoseModule as pm

path = "K:\PROJECT\AI_GYM_TRAINER"

def DPU():
    exec(open(path+"\DECLINE_PUSH_UP.py").read())
def IPU():
    exec(open(path+"\INCLINE_PUSH_UP.py.py").read())
def DC():
    exec(open(path+"\DUMBBELL_CURLS.py").read())
def DR():
    exec(open(path+"\DUMBBELL_ROW.py").read())
def GB():
    exec(open(path+"\GLUTE_BRIDGE.py").read())
def GP():
    exec(open(path+"\GROUND_PULLY.py").read())
def HC():
    exec(open(path+"\HAMMER_CURLS.py").read())
def P():
    exec(open(path+"\PLANK.py").read())
def PU():
    exec(open(path+"\PUSHUP.py").read())
def SSPU():
    exec(open(path+"\SIDE_SHOULDER_RAISE.py").read())
def TBR():
    exec(open(path+"\T_BAR_ROW.py").read())
def TPD():
    exec(open(path+"\TRICEP_PUSH_DOWN.py").read())

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
        
    