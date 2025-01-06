include <Servo.h> Servo servoMain; // Define our Servo

int trigpin = 10;
int echopin = 11;
int distance;
float duration;
float cm;

void setup()
	servoMain.attach(9); // servo on digital pin 10
	pinMode(trigpin, OUTPUT);
	pinMode(echopin, INPUT);

void loop()
	digitalWrite(trigpin, LOW);
	delay(2); 
	digitalWrite(trigpin, HIGH);
	delayMicroseconds(10);

	digitalWrite(trigpin, LOW);

	duration = pulseIn(echopin, HIGH);
	cm = (duration/58.82); distance = cm;
	if(distance>10)
		servoMain.write(905); // Turn Servo back to center position (90 degrees)
		delay(50);
	else
		servoMain.write(0);