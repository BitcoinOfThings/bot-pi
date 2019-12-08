import Adafruit_DHT
import paho.mqtt.client as mqtt
import json

mqttc = mqtt.Client()
mqttc.username_pw_set(username="demo", password="demo")
mqttc.connect("mqtt.bitcoinofthings.com")

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

print ("Reading DHT22...")
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        mqttc.publish("bot_demo", json.dumps({"clientId":"demo", "message":"{0:0.1f}".format(temperature)}))
    else:
        print("Failed to retrieve data from humidity sensor")

