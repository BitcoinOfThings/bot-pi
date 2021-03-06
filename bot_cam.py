from picamera import PiCamera
from time import sleep
import paho.mqtt.client as mqtt
import json
import os.path
import sys
import datetime

CAMFILE = "bot.jpg"
CAMHEIGHT = 200 
CAMWIDTH = 300
CAMWAIT = 54
topic = "demo/cam"

def take_pic():
    camera = PiCamera()
    camera_annotate_text_size = 32
    camera.framerate = 15
    camera.resolution = (CAMWIDTH, CAMHEIGHT)
    #camera.image_effect = 'cartoon'
    camera.start_preview(alpha=200)
    #camera.start_recording('bot.h264')
    sleep(5)
    #camera.stop_recording()
    dt = datetime.datetime.now().ctime()
    camera.annotate_text = "BitcoinOfThings.com {0}".format(dt)
    camera.capture(CAMFILE)
    camera.stop_preview()
    camera.close()
    return dt

mqttc = mqtt.Client()
mqttc.username_pw_set(username="demo", password="demo")
mqttc.connect("mqtt.bitcoinofthings.com")

print('publishing pics to {0}'.format(topic))

try:
    while True:
        dt = take_pic()
        if os.path.isfile(CAMFILE):
            with open(CAMFILE, mode='rb') as file:
                contents = file.read()
                # todo: if posting to blockchain need to fix the fee for large files
                pic = contents.hex() #[0:25]
                #print(pic)
                jMessage = {"clientId":"demo", "message": pic}
                #print(jMessage)
                #mqttc.publish(topic, 'pic {0}'.format(dt))
                mqttc.publish(topic, json.dumps(jMessage))
                print("{0}: published pic".format(dt))
            os.remove(CAMFILE)
        else:
            print("No picture taken")
        sleep(CAMWAIT)
except KeyboardInterrupt:
    sys.exit()

