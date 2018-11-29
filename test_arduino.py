import serial #Serial imported for Serial communication
import time #Required to use delay functions
ArduinoSerial = serial.Serial('/dev/cu.usbmodem141301',9600)
time.sleep(2)
print (ArduinoSerial.readline())
ArduinoSerial.write('1')
while True:
    var = raw_input() #get input from user
    print ("you entered", var) #print the input for confirmation
   
    if (var == '1'): #if the value is 1
        ArduinoSerial.write('1') #send 1
        print ("LED turned ON")

    if (var == '0'): #if the value is 0
        ArduinoSerial.write('0') #send 0
        print ("LED turned OFF")
    print (ArduinoSerial.readline())

