1.	import RPi.GPIO as GPIO     #importing GPIO module from RPi package as GPIO
2.	GPIO.setmode(GPIO.BOARD)    #setting GPIO access mode as BOARD
3.	GPIO.setwarnings(False)     #setting warnings false
4.	from time import sleep      #importing sleep module from time package
5.	 
6.	GPIO.setup(8,GPIO.IN)       #setting 8th pin as input pin for MQ-03 sensor
7.	 
8.	GPIO.setup(10,GPIO.OUT)     #setting 10th pin as output pin for engine 
9.	 
10.	 
11.	while True:                 #inifite loop for alcohol detection
12.	    if GPIO.input(8) :      #checking alcohol if not detected it will allow to start the engine
13.	        print("not detected",GPIO.input(8))  #returns not detected
14.	        GPIO.output(10,1)   #turning ON engine
15.	    else:                   #if alcohol detected it will not allow to start the engine
16.	        print("alcohol detected",GPIO.input(8))  #returns alcohol detected
17.	        GPIO.output(10,0)   #turning OFF engine
18.	    sleep(0.5)              #stops execution for 0.5 seconds
