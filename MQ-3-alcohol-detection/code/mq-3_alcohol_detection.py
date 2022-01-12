import RPi.GPIO as GPIO     #importing GPIO module from RPi package as GPIO
GPIO.setmode(GPIO.BOARD)    #setting GPIO access mode as BOARD
GPIO.setwarnings(False)     #setting warnings false
from time import sleep      #importing sleep module from time package
 
GPIO.setup(8,GPIO.IN)       #setting 8th pin as input pin for MQ-03 sensor
 
GPIO.setup(10,GPIO.OUT)     #setting 10th pin as output pin for engine 
 
 
while True:                 #inifite loop for alcohol detection
    if GPIO.input(8) :      #checking alcohol if not detected it will allow to start the engine
        print("not detected",GPIO.input(8))  #returns not detected
        GPIO.output(10,1)   #turning ON engine
    else:                   #if alcohol detected it will not allow to start the engine
        print("alcohol detected",GPIO.input(8))  #returns alcohol detected
        GPIO.output(10,0)   #turning OFF engine
    sleep(0.5)              #stops execution for 0.5 seconds