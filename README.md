# Automatic-Packing-Control-Machine
Design and Implementation of a affordable and efficient ,packing control machine for industrial application.

Objectives
1 . To construct Automatic Hopper Filling unit using Arduino and Sensors.
2 . To work on software related to overall functional units of the machine.
3 . To design and construct stand and heating element
4 . To assemble the project and work on hardware and software improvements.

Methadology
• Main Conveyor unit consist of conveyor belt, two Rollers, parallel shaft, spur gear arrangement with ball bearings.
• There are two Infrared sensors fixed on the stand frame with three dc motors and corresponding relay units R1( Conveyor belt control), R2(Hopper opening), R3(Heater move-ment).
• The operation of packing is started when raspberry board receives signal from the IR sensors.

AT NORMAL CONDITION
IR transmitter sensor is transmitting the IR rays using 555 IC Timer, These rays are received by IR receiver sensor. So time relay is OFF and conveyor runs continuously.

AT OBSTACLE CONDITION
At Obstacle Condition the resistance across transmitter and receiver is HIGH due to non conducting of IR waves so relay becomes ON and signals are given to controlling unit. When there is an obstacle in IR sensor 1 and these signals act as interrupt signal to Raspberry Pi ,In that moment time Relay R1 is OFF and Relay R3 becomes ON for 1 seconds and once again ON Relay R1,The above procedure is repeated once again for other work piece.

<img width="427" alt="image" src="https://github.com/user-attachments/assets/717cd7fe-c7e8-4767-9db8-eee388378671" />

<img width="367" alt="image" src="https://github.com/user-attachments/assets/7c953b35-059b-4ba7-b21b-fe37f12a3017" />

