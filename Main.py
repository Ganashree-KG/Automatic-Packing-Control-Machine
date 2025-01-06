import RPi.GPIO as GPIO
import time

ir_sensor_1 = 27
ir_sensor_2 = 22
conveyor_relay = 26
pack_relay_1 = 5
pack_relay_2 = 7

GPIO.setmode (GPIO.BCM) #set to port mode
GPIO.setup(ir_sensor_1, GPIO.IN)
GPIO.setup(ir_sensor_2, GPIO.IN)
GPIO.setup(conveyor_relay, GPIO.OUT)
GPIO.setup(pack_relay_1, GPIO.OUT)
GPIO.setup(pack_relay_2,GPIO.OUT) GPT GPIO.output(conveyor_relay, False)

print "IR Sensor Ready....."
#on always initially
print ""

while True:
	GPIO.output(conveyor_relay, GPIO.LOW)

	if GPIO.input(ir_sensor_1) == True:
		GPIO.output(conveyor_relay, GPIO.LOW)
		GPIO.output(pack_relay_1, GPIO.HIGH)
		print "Object Detected"
		time.sleep(3)
		GPIO.output(conveyor_relay, GPIO.HIGH)
		GPIO.output(pack_relay_1, GPIO.LOW)
	if GPIO.input(ir_sensor_2):
		GPIO.output(conveyor_relay, GPIO.LOW)
		GPIO.output (pack_relay_2, GPIO.HIGH)
		print "Object Detected"
		time.sleep(3)
		GPIO.output(conveyor_relay, GPIO.HIGH)
		GPIO.output(pack_relay_2,GPIO.LOW)