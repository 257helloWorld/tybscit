# Controlling Raspberry Pi with Telegram.

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# LED
def on(pin):
    GPIO.ouput(pin, GPIO.HIGH)

def off(pin):
    GPIO.output(pin, GPIO.LOW)

ledPin = 11

def handle(msg):
    # chat_id = msg['chat']['id']
    command = msg['text'].lower()
    print(f"Got command: {command}")
    if command == 'on':
        on(ledPin)
    elif command == 'off':
        off(ledPin)

bot = telepot.Bot("Token")

bot.message_loop(handle)
print("I am listening")

while(True):
    time.sleep(10)