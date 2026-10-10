# Skylog-pcb
This is a PCB Im making for my rc plane and rocket! It will track velocity, distance, time, acceleration, gps, have a buzzer and a servo module to release a parachute on apogee!!

I created this for my school club as well, where we test out rc planes and would love to add this addition and teach the cub how to make a pcb. 

I first started with an idea and a name sky logger. I'v always thought about creating pcbs but thought they were to intercate and difficult. I learned that the best way to learn is to do, so instead of watching a youtube video I went right into it, were I succesfully created this amazing pcb, my first ever. I first started with a list of parts that I will probably use. This consisted of a gps, buzzer, led, distance and velocity tracker, esp32 Pico and more. I placed these parts into the schematic and started routing everything up, which took quite a lot of time. After this, I went into the PCB editor and placed everything onto the rough retangular cutout. Routing the traces reminded me of that one game were you have to connect the dots with wires but the wires can't touch each other. This was the fun and also a frustrating part as well. One way I was able to make this much easier was buy learning how to add a fill zone. This filled the back layer with copper which connected to the GND pads, letting me cleanup my whole board nicely and allowing routing to be easier. I added labels so I know were each part goes to and which way they connect. I also added some art! I got this art from Claude, and it I thought It looked very nice. Overall this was an amazing experience and my firs time creating the PCB went well. A sad part is the cost. The PCB is quite expensive to ship to the UAE and same with some of the parts. 



## Parts

### On the board

| Ref | Part | Value | Package | Purpose |
|---|---|---|---|---|
| A1 | Raspberry Pi Pico | RP2040 | THT module, on 2x 1x20 female headers | Main microcontroller |
| U1 | W25Q64JV | 64 Mbit flash | SOIC-8 (208 mil) | Stores flight data |
| Q1 | 2N7002 | N-channel MOSFET | SOT-23 | Switches the buzzer |
| D1 | 1N5819HW | Schottky diode | SOD-123 | Stops battery and USB from feeding each other |
| D2 | LED | Status LED | 0603 | Power and status light |
| R1 | Resistor | 100 Ω | 0603 | Q1 gate resistor |
| R2 | Resistor | 10 kΩ | 0603 | Holds Q1 gate low at boot |
| R3 | Resistor | 330 Ω | 0603 | LED current limit |
| R4, R5 | Resistor | 100 kΩ | 0603 | Battery voltage divider |
| R6 | Resistor | 10 kΩ | 0603 | Flash chip-select pull-up |
| C1 | Electrolytic capacitor | 100 µF | Radial, 6.3 mm | Servo power smoothing |
| C2, C3 | Capacitor | 100 nF | 0603 | Decoupling and ADC filter |
| SW1 | SS12D00G4 | Slide switch | 1x3, 2.54 mm | Power switch |
| J1 | Socket | 1x4 | 2.54 mm | BMP280 barometer |
| J2 | Socket | 1x4 | 2.54 mm | GPS (plane only) |
| J3 | Socket | 1x8 | 2.54 mm | MPU6050 IMU |
| J4 | JST B2B-PH-K | 2-pin | JST-PH, 2.00 mm | 1S LiPo battery |
| J5 | Header | 1x2 | 2.54 mm | Buzzer |
| J6 | Header | 1x3 | 2.54 mm | Servo |
| J7 | Header | 1x2 | 2.54 mm | Mode jumper (rocket or plane) |

### Plugged in or attached

| Part | Connects to | Notes |
|---|---|---|
| BMP280 module (3.3 V) | J1 | Pressure and altitude |
| GY-521 (MPU6050) module | J3 | Motion and orientation |
| GPS module (NEO-6M type) | J2 | Plane only |
| SG90 servo | J6 | Parachute release |
| Active buzzer, 2-wire | J5 | Locator beeper |
| 1S LiPo with JST-PH plug | J4 | Power. Never plug a 3S pack |
