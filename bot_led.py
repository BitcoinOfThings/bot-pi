# listens for mqtt messages and controls led connected to rpi

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json

#
LED = 32

def on_message(client, userdata, message) :
    try:
        #print(message.payload)
        msg = json.loads(message.payload.decode('utf8'))
        #print(msg["message"])
        val = int(msg["message"])
        print(val)
        if (val == 0):
            GPIO.output(LED, GPIO.LOW)
        else:
            GPIO.output(LED, GPIO.HIGH)
    except Exception as ex:
        print(ex)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

mqttc = mqtt.Client()
mqttc.username_pw_set(username="demo", password="demo")
mqttc.connect("mqtt.bitcoinofthings.com")
#mqttc.loop_start()
mqttc.on_message = on_message
mqttc.subscribe("demo")
try :
    print("Send 0 or 1 to bot_demo to turn the LED on or off")
    mqttc.loop_forever()
except KeyboardInterrupt:
    pass
#cleanup resets the pin therefore the led will be shut off
GPIO.cleanup()

