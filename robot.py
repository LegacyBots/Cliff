import RPi.GPIO as GPIO
from time import sleep

pwm_A = 0
pwm_B = 0

# Pins for Motor Driver Inputs 
Motor1A = 14
Motor1B = 15
Motor1E = 18


Motor2A = 5
Motor2B = 6
Motor2E = 13

def motorStop():#Motor stops
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)
    
def Motor():
    
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    pwm_B.start(100)
    pwm_B.ChangeDutyCycle(speed)

    

 
def setup():
    global pwm_a, pwm_b
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)              
    GPIO.setup(Motor1A,GPIO.OUT)  
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)            
    GPIO.setup(Motor2A,GPIO.OUT)  
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
    try:
        pwm_A = GPIO.PWM(Motor1E, 1000)
        pwm_B = GPIO.PWM(Motor1E, 1000)
    except:
        pass
 
def loop():
    # Going forwards
    Motor()
    print("Going forwards")
 
    sleep(5)
    # Going backwards

    print("Going backwards")
 
    sleep(5)
    # Stop

    print("Stop")

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':     
    setup()
    try:
            loop()
    except KeyboardInterrupt:
        destroy()