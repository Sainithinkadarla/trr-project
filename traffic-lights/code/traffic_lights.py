import RPi.GPIO as GPIO #importing GPIO module from RPi package as GPIO
import time #importing time module 
GPIO.setwarnings(False) #setting warnings false
GPIO.setmode(GPIO.BOARD) #setting GPIO access mode as BOARD
#display setup output pins
GPIO.setup(8, GPIO.OUT)     	#GPIO19
GPIO.setup(10, GPIO.OUT)    	#GPIO18
GPIO.setup(12, GPIO.OUT)     	#GPIO16
GPIO.setup(16, GPIO.OUT)     	#GPIO13
GPIO.setup(18, GPIO.OUT)     	#GPIO23
GPIO.setup(22, GPIO.OUT)     	#GPIO20
GPIO.setup(24, GPIO.OUT)    	#GPIO21
 
#LED setup output pins
GPIO.setup(26,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
 
#buzzer setup output pins
GPIO.setup(38,GPIO.OUT)
#configuration 7 segment digits
digitclr=[1,1,1,1,1,1,1]
digit0=[0,0,0,0,0,0,1]  #[a,b,c,d,e,f,g]
digit1=[1,0,0,1,1,1,1]
digit2=[0,0,1,0,0,1,0]
digit3=[0,0,0,0,1,1,0]
digit4=[1,0,0,1,1,0,0]
digit5=[0,1,0,0,1,0,0]
digit6=[0,1,0,0,0,0,0]
digit7=[0,0,0,1,1,1,1]
digit8=[0,0,0,0,0,0,0]
digit9=[0,0,0,0,1,0,0]
gpin=[10,8,24,22,18,12,16]
#storing all 7 segment digit configuration in digits list
digits=[digit0,digit1,digit2,digit3,digit4,digit5,digit6,digit7,digit8,digit9]
 
#routine to clear and then write to display
def digdisp(digit):
   for x in range (0,7):
      GPIO.output(gpin[x], digitclr[x])
   for x in range (0,7):
      GPIO.output(gpin[x], digit[x])
def timer(color):
    for i in range(9,-1,-1):
        if color=='red':
            if i==2:
                GPIO.output(38,0) #turns on buzzer
            if i==0:
                GPIO.output(38,1) #turns off buzzer 
        digdisp(digits[i])
        time.sleep(1)
 
while True:
    GPIO.output(26,0) #turns on red LED 
    timer('red') #shows 10 seconds timer
    GPIO.output(26,1) #turns off red LED
    GPIO.output(36,0) #turns on green LED 
    timer('green') #shows timer 9-0 
    GPIO.output(36,1) #turns off green LED 
    GPIO.output(32,0) #turns on yellow LED 
    GPIO.output(38,0) #turns on buzzer
    time.sleep(2) #waits for two seconds
    GPIO.output(38,1) #turns off buzzer 
    GPIO.output(32,1) #turns off yellow LED
 