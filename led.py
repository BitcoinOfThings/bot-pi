import RPi.GPIO as GPIO		#import RPi.GPIO module

LED = 32			#pin no. as per BOARD, GPIO18 as per BCM
Switch_input = 29		#pin no. as per BOARD, GPIO27 as per BCM
GPIO.setwarnings(False) 	#disable warnings
GPIO.setmode(GPIO.BOARD)	#set pin numbering format
GPIO.setup(LED, GPIO.OUT)	#set GPIO as output
GPIO.setup(Switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    #if (GPIO.input(Switch_input)):
    #GPIO.output(LED,GPIO.LOW)
    #else:
    GPIO.output(LED,GPIO.HIGH)

