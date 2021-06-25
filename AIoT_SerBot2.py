import BlynkLib
from pop import Pilot, LiDAR
import math
import random
import time
import pyaudio
import numpy as np
from pop import Tone
import subprocess
import multiprocessing as mp
from gtts import gTTS

BLYNK_AUTH = 'xkRpHiPDTfY3TZVPLGcYntK76Nb7AkCa'
blynk = BlynkLib.Blynk(BLYNK_AUTH)  # server = '10.10.11.57, port=9443

bot = Pilot.SerBot()

@blynk.VIRTUAL_WRITE(0)
def switch(n):
    
    if int(n[0])==1:
        bot.forward(5)
        bot.steering = -1.0
        print("left turn")

    elif int(n[0])==2:
        bot.stop()
        print("stop")

    elif int(n[0])==3:
        bot.forward(5)
        bot.steering = 1.0 
        print("right turn")

@blynk.VIRTUAL_WRITE(1)
def effet(n):
    
    if int(n[0])==1:
        with subprocess.Popen(['play', 'siren1.mp3']) as p:
            p.play()
        
    elif int(n[0])==2:
        with subprocess.Popen(['play', 'siren2.mp3']) as p:  
            p.play()
    
    elif int(n[0])==3:
        with subprocess.Popen(['play', 'siren3.mp3']) as p:  
            p.play()

    elif int(n[0])==4:
            p.stop()

x = 512 
y = 512

@blynk.VIRTUAL_WRITE(2)
def v4_write_hander(value):
    global x
    
    x = value
    print("1번 : ",type(value),value)

@blynk.VIRTUAL_WRITE(3)
def joystick(value):
    global y
    y = value
    print("2번 : ",type(value),value)

    if 500< int(x[0]) < 550 and 500 < int(y[0]) < 550 :
        bot.stop()

    if 50< int(x[0]) <350 and 800 < int(y[0]) <= 1023 :   # 대각선 왼쪽 위
        bot.forward(40)
        bot.steering = -0.5
    if 700 < int(x[0]) < 1000 and 600 < int(y[0]) <= 1023 : # 대각선 오른쪽 위 
        bot.forward(40)
        bot.steering = 0.5
    if 50 < int(x[0]) < 300 and 50 < int(y[0]) < 300 : # 대각선 왼쪽 아래
        bot.backward(40)
        bot.steering = -0.5
    if 800 < int(x[0]) < 1000 and 100 < int(y[0]) < 300 : # 대각선 오른쪽 아래
        bot.backward(40)
        bot.steering = 0.5
    if 450 < int(x[0]) < 650 and 850 < int(y[0]) <= 1023 :  #위
        bot.move(0, 50)
    if 0 <= int(x[0]) < 150 and 400 < int(y[0]) < 650 :  # 왼쪽
        bot.move(270, 50)
    if 1000 < int(x[0]) <= 1023 and 400 < int(y[0]) < 600 : # 오른쪽
        bot.move(90, 50)
    if 200 < int(x[0]) < 600 and 0 <= int(y[0]) < 100 :  # 아래
        bot.move(180, 50)

while True:
    try:
        blynk.run()
    except IOError:
        pass


