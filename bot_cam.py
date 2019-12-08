from picamera import PiCamera
from time import sleep
import paho.mqtt.client as mqtt
import json
import os.path
import sys

CAMFILE = "bot.jpg"
CAMWAIT = 10

def take_pic():
    camera = PiCamera()
    camera_annotate_text_size = 60
    camera.annotate_text = "Uploaded using BitcoinOfThings.com"
    camera.framerate = 15
    camera.resolution = (800, 600)
    camera.image_effect = 'cartoon'
    camera.start_preview(alpha=200)
    #camera.start_recording('bot.h264')
    sleep(5)
    #camera.stop_recording()
    camera.capture(CAMFILE)
    camera.stop_preview()
    camera.close()

mqttc = mqtt.Client()
mqttc.username_pw_set(username="demo", password="demo")
mqttc.connect("mqtt.bitcoinofthings.com")

try:
    while True:
        take_pic()
        if os.path.isfile(CAMFILE):
            with open(CAMFILE, mode='rb') as file:
                contents = file.read()
                jMessage = {"clientId":"demo", "message": contents.hex()}
                mqttc.publish("bot_demo", json.dumps(jMessage))
                print("published picture")
            os.remove(CAMFILE)
        else:
            print("No picture taken")
        sleep(CAMWAIT)
except KeyboardInterrupt:
    sys.exit()

