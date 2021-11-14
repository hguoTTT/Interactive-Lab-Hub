import time
import board
import busio
import qwiic_joystick

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/your/topic/here'

myJoystick = qwiic_joystick.QwiicJoystick()

myJoystick.begin()

while True:
    val = "X: %d, Y: %d, Button: %d" % ( \
					myJoystick.horizontal, \
					myJoystick.vertical, \
					myJoystick.button)
    print(val)
    client.publish(topic, val)
    time.sleep(0.25)
