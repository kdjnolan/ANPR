import RPi.GPIO as GPIO		   	#import libs
import time

PWMpin = 12						#specify pin			

dutyCycle = 90     				#set dutycycle between 0-100

GPIO.setmode(GPIO.BOARD)	   	#set BOARD gpio numbering mode

GPIO.setup(PWMpin, GPIO.OUT)	#setup pin 12 as an output




#p = GPIO.PWM(channel, frequency)
pwm = GPIO.PWM(pwmPin, 50)      #init PWM with 50Hz frequency

pwm.start(dutyCycle)			#start PWM on selected pin



pwm.ChangeFrequency(freq)			#change frequency
pwm.ChangeDutyCycle(dc)			#change the duty cycle

pwm.stop()						#stops pwm

GPIO.cleanup()
