import pygame
import board
import busio
import time
import paho.mqtt.client as mqtt
import uuid
import signal

from gtts import gTTS
from word2number import w2n
import speech_recognition as sr
import os
import random

import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# ======================= record voices =====================================

PauseText = 'Music Paused'
PlayText = 'Music Continued'

language = 'en'
mPause = gTTS(text=PauseText, lang=language, slow=False)
mPlay = gTTS(text=PlayText, lang=language, slow=False) 

mPause.save("mpause.mp3")
mPlay.save("mplay.mp3")

# ======================= Controls ==========================================

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)


#================================ music player ===============================================

pygame.init()
pygame.mixer.init()

def play(x):
    pygame.mixer.music.load(x)
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
    
song = "test.mp3"
play(song)

isPause = False

#Set up speech recognition
r = sr.Recognizer()
    
while True:
    string = song
    
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    
    if not buttonA.value:
        pause()
        with sr.Microphone() as source:
            audio = r.listen(source)
        response = r.recognize_sphinx(audio)
        print("DEBUG:" + reponse)
        if response == "pause":
            os.system("mplayer mpause.mp3")
            isPause = True
            continue
        elif response == "play":
            os.system("mplayer mplay.mp3")
            isPause = False
            unpause()
            continue
        if isPause == False:
            unpause()
    
    '''
    if not buttonA.value:
        pause()
    if not buttonB.value:
        unpause()    
    '''
    draw.text((0, 0), string, font=font, fill=(240,255,255))
    
    disp.image(image, 90)
    time.sleep(.01)
