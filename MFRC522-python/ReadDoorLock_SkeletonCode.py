#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time


GPIO.setmode(GPIO.BCM)
ServoPin = 23
GreenLED = 21
RedLED = 20

GPIO.setup(GreenLED, GPIO.OUT)
GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(ServoPin, GPIO.OUT)
Servo = GPIO.PWM(ServoPin,50)
Servo.start(5)

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print"Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

        #change xxx, yyy, zzz, and www to match the UIDs from the Read.py program output
        if ((uid[0] == '''xxx''') and  (uid[1] == '''yyy''') and  (uid[2] == '''zzz''') and  (uid[3] == '''www''')):
            #add your code here:
            print "Access Granted\n" #prompt the user that they have access

            #turn on the green LED

            #change the duty cycle to 12% for the servo (make the servo move 180 degrees)

            #make the Raspberry Pi wait for 5 seconds

            #change the duty cycle to 5% for the servo (make the servo move 0 degrees)

            #make the Raspberry Pi wait for 1 second

            #turn off the green LED

        else:
            print "Access Denied\n" #prompt the user that they don't have access
            #turn on the Red LED

            #make the Raspberry Pi wait for 5 seconds

            #turn off the Red LED
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

