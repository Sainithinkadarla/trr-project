from machine import Pin,PWM#importing Pin module from machine package
from time import sleep#importing sleep module from time package
import utime#importing utime module for micro seconds


MotorL1 = Pin(6,Pin.OUT)
MotorL2 = Pin(5,Pin.OUT)
MotorR1 = Pin(4,Pin.OUT)
MotorR2 = Pin(3,Pin.OUT)
MotorEN = Pin(2,Pin.OUT)

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

MID=1300000
MIN=0250000
MAX=2300000

pwm=PWM(Pin(1))
pwm.freq(50)
pwm.duty_ns(MID)

def get_distance(str):
   trigger.low()
   echo.low()
   print("distance fetching started")
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   #timepassed=0
   print("distance fetching started")
   
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   print("distance fetching started")
   timepassed = signalon - signaloff
   
   global distance
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm",str)
   return distance

def m_forward():
    print('Forward')
    MotorL1.value(1)
    MotorL2.value(0)
    MotorR1.value(1)
    MotorR2.value(0)
    MotorEN.value(1)

def m_reverse():
    print('Reverse')
    MotorL1.value(0)
    MotorL2.value(1)
    MotorR1.value(0)
    MotorR2.value(1)
    MotorEN.value(1)

def m_right():
    print('Right')
    MotorL1.value(1)
    MotorL2.value(0)
    MotorR1.value(0)
    MotorR2.value(1)
    MotorEN.value(1)
    
def m_left():
    print('Left')
    MotorL1.value(0)
    MotorL2.value(1)
    MotorR1.value(1)
    MotorR2.value(0)
    MotorEN.value(1)

def m_stop():
    print('Stop')
    MotorL1.value(0)
    MotorL2.value(0)
    MotorR1.value(0)
    MotorR2.value(0)
    MotorEN.value(0)

def s_front():
    pwm.duty_ns(MID)
    sleep(2)

def s_right():
    pwm.duty_ns(MIN)
    sleep(2)

def s_left():
    pwm.duty_ns(MAX)
    sleep(2)


def inactive():
    m_stop()
    pwm.duty_ns(0)
    trigger.low()
    echo.low()


inactive()
sleep(2)
m_forward()#



while True:
    #inactive()
    get_distance("front")
    print("front")
    if distance<=7:
        m_stop()#
        s_left()
        l_dist=get_distance("left")
        sleep(1)
        s_right()
        r_dist=get_distance("right")
        s_front()
        if l_dist>r_dist:
            print("Move for 2 sec")
            m_left()#
            sleep(1)
            print("move left")
            m_left()#
            m_forward()
            f_dist=get_distance("front")
            
        else:
            print("Move for 2 sec")
            m_right()#
            sleep(1)
            print("move right")
            m_right()#
            m_forward()
            print("front")
            f_dist=get_distance("front")

    else:
        m_forward()
else:
    m_forward()
        

