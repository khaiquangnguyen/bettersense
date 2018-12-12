import paho.mqtt.client as mqtt
import os, urlparse
import serial #Serial imported for Serial communication
import time #Required to use delay functions
ArduinoSerial = serial.Serial('/dev/cu.usbmodem141110',9600)
time.sleep(2)
print (ArduinoSerial.readline())

global n
n = 0
# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    global n 
    n+=1
    print(str(n) + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if msg.payload == "1":
        ArduinoSerial.write('10') #send 1
    if msg.payload == "red":
        ArduinoSerial.write('20') #send 1
    if msg.payload == "yellow":
        ArduinoSerial.write('30') #send 1
    if msg.payload == "green":
        ArduinoSerial.write('40') #send 1
    if msg.payload == "aqua":
        ArduinoSerial.write('50') #send 1
    if msg.payload == "orange":
        ArduinoSerial.write('60') #send 1
    if msg.payload == "blue":
        ArduinoSerial.write('70') #send 1
    if msg.payload == "white":
        ArduinoSerial.write('80') #send 1

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log


# Connect
mqttc.username_pw_set('vswyqwhc', 'G4Mx5iGkb5Ol')
mqttc.connect("m15.cloudmqtt.com", 16819)

# Start subscribe, with QoS level 0
mqttc.subscribe("/bettersense", 0)

# Publish a message
mqttc.publish("/bettersense", "my message")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))



# while True:
#     var = raw_input() #get input from user
#     print ("you entered", var) #print the input for confirmation
#     if (var == '1'): #if the value is 1
#         ArduinoSerial.write('1') #send 1
#         print ("LED turned ON")

#     if (var == '0'): #if the value is 0
#         ArduinoSerial.write('0') #send 0
#         print ("LED turned OFF")
#     print (ArduinoSerial.readline())



