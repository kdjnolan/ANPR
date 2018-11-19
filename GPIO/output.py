import RPi.GPIO as GPIO		   #import libs
import time

GPIO.setmode(GPIO.BOARD)	   #set BOARD gpio numbering mode
GPIO.setup(12, GPIO.OUT)	   #setup pin 12 as an output

while(1):
	GPIO.output(12, GPIO.HIGH) #set high
	time.sleep(1)
	GPIO.output(12, 0)		   #set low
	time.sleep(1)
	
GPIO.cleanup() 					#release any resources the script is using
