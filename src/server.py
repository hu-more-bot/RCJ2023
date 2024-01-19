# About:
# This code is for the 2023 RoboCup Junior Competetion in OnStage Category
# for the HU-MORE-BOT Team's presentation
# I don't use python (once a year at most), so this is quite the spaghetti, but i don't care
# because i am writing Python code, so speed is clearly not the main priority

import bt
import RPi.GPIO as GPIO
import time
import os

print("---- Start ----")

# Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(15, GPIO.OUT)

# Blink [count] times with a delay of [timing]
def blink(count = 3, timing = 0.2):
    for i in range(count):
        GPIO.output(15, 1)
        time.sleep(timing)
        GPIO.output(15, 0)
        time.sleep(timing)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Button Trigger -> Send Message
def trigger(message, timeout=1):
    GPIO.wait_for_edge(14, GPIO.FALLING)
    time.sleep(timeout)
    bt.send(message)

# Main Code
try:
    # Wait to connect
    print("Waiting to connect...")
    GPIO.output(15, 1)
    GPIO.wait_for_edge(14, GPIO.FALLING)

    GPIO.output(15, 0)

    # Init Bluetooth
    print("Connecting...")
    blink(2)

    bt = bt.BT(True)

    if bt.clients == 0:
        print("No Clients Connected, exiting...")
        for i in range(3):
            blink(5)
        exit()

    print("Connected to " + str(bt.clients) + " Client(s)")

    blink(bt.clients, 0.5)

    GPIO.output(15, 1)

    # Start
    trigger(bytes(str("start"), 'utf-8'))
    print("Started")
    blink(2)

    time.sleep(63-0.4)

    bt.send("dance")

    # End
except KeyboardInterrupt:
    pass

#bt.destroy()
print("---- End ----")
blink(5)