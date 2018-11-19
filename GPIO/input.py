import RPi.GPIO as GPIO		   	#import libs
import time

GPIO.setmode(GPIO.BOARD)	   	#set BOARD gpio numbering mode
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#setup pin as an input, pulled down(disabled if not specified)

while(1):
	if GPIO.input(17):
		print("Pin is HIGH")
	else:
		print("Pin is LOW")
	time.sleep(1000)

GPIO.cleanup() 					#release any resources the script is using


