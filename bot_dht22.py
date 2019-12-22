import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import time
import datetime

mqttc = mqtt.Client()
mqttc.username_pw_set(username="demo", password="demo")
mqttc.connect("mqtt.bitcoinofthings.com")

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
topic = "demo/temp"

print("publishing on {0}".format(topic))
print ("Reading DHT22...")
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        dt = datetime.datetime.now().ctime()
        msgtext = '{0}: Temp={1:0.1f}*C Humidity={2:0.1f}%'.format(dt, temperature, humidity)
        print(msgtext)
        mqttc.publish(topic, json.dumps({"clientId":"demo", "message":msgtext}))
        time.sleep(60)
    else:
        print("Failed to retrieve data from humidity sensor")

