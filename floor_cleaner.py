from machine import Pin,PWM #importing Pin module from machine package
from time import sleep #importing sleep module from time package
import utime #importing utime module for micro seconds
	 
#setting up motor pins 
MotorL1 = Pin(3,Pin.OUT)
MotorL2 = Pin(4,Pin.OUT)
MotorR1 = Pin(5,Pin.OUT)
MotorR2 = Pin(6,Pin.OUT)
MotorEN = Pin(2,Pin.OUT)
	
#setting up ultrasonic distance sensor pins 
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
 
#microseconds for servo motor rotation
MID=1300000
MIN=350000
MAX=2300000
	
#setting up servo motor PWM pin
pwm=PWM(Pin(1))
pwm.freq(50)
pwm.duty_ns(MID)
	 
def get_distance(str):
   trigger.low() #making trigger low to reset
   echo.low() #making echo low to reset 
   print("distance fetching started")
   trigger.low() #makingtrigger low for calculation 
   utime.sleep_us(2) #waits for 2 microseconds
   trigger.high() #making trigger high 
   utime.sleep_us(5) #waits for 2 microseconds
   trigger.low() #making trigger low
   
   print("distance fetching started")
   
   while echo.value() == 0: #checks echo as value or not
       signaloff = utime.ticks_us() #stores initial micro time
   while echo.value() == 1: #checks echo as value or not
       signalon = utime.ticks_us() #stores final micro time
   print("distance fetching started")
   timepassed = signalon-signaloff #calculates actual time
   
   global distance #making distance variable as global 
   distance = (timepassed * 0.0343) / 2 #calculating distance
   print("The distance from object is ",distance,"cm",str) 
   return distance #returns distance
 
def m_forward(): #moves forward
    print('Forward')
    MotorL1.value(1)
    MotorL2.value(0)
    MotorR1.value(1)
    MotorR2.value(0)
    MotorEN.value(1)
	 
def m_reverse(): #moves backward
    print('Reverse')
    MotorL1.value(0)
    MotorL2.value(1)
    MotorR1.value(0)
    MotorR2.value(1)
    MotorEN.value(1)
	 
def m_right(): #turnss right
    print('Right')
    MotorL1.value(1)
    MotorL2.value(0)
    MotorR1.value(0)
    MotorR2.value(1)
    MotorEN.value(1)
	    
def m_left(): #turns left 
    print('Left')
    MotorL1.value(0)
    MotorL2.value(1)
    MotorR1.value(1)
    MotorR2.value(0)
    MotorEN.value(1)
	 
def m_stop(): #stop 
    print('Stop')
    MotorL1.value(0)
    MotorL2.value(0)
    MotorR1.value(0)
    MotorR2.value(0)
    MotorEN.value(0)
	 
def s_front(): #servo motor will face forward
    pwm.duty_ns(MID)
    sleep(2)
 
def s_right(): #servo motor will turn right
    pwm.duty_ns(MIN)
    sleep(2)
	 
def s_left(): #servo motor will turn left
    pwm.duty_ns(MAX)
    sleep(2)
	 
	 
def inactive(): #inactives all pins or makes all pins low
    m_stop()
    pwm.duty_ns(0)
    trigger.low()
    echo.low()
    
	 
	 
inactive() #making all pins low
sleep(2) #waits for 2 seconds
m_forward() #moves forward
	 
	 
	 
while True: 

    get_distance("front") #calculating front distance
    print("front")
    if distance<=5: #checks if distance 
       m_stop() #stop 
       s_left() #servo motor turns left
       l_dist=get_distance("left") #calculating left distance
       sleep(1) #waits for 2 seconds
       s_right() #servo motor turns right
       r_dist=get_distance("right") #calculating right distance
       s_front() #servo motor will face forward
       if l_dist>r_dist: #checks left distance is greater than right distance
            print("Move for 2 sec")
            m_left() #turns left
            sleep(2) #waits for 2 seconds
            print("move left")
            m_left() #turns left
            m_forward() #moves forward
            f_dist=get_distance("front") #calculating front distance
       else:
            print("Move for 2 sec")
            m_right() #turns right
            sleep(2) #waits for 2 seconds
            print("move right")
            m_right() #turns right
            m_forward() #moves forward
            print("front")
            f_dist=get_distance("front") #calculating front distance
	 
    else:
        m_forward() #moves forward
else:
    m_forward() #moves forward