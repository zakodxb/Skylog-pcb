# Skylog-pcb
This is a PCB Im making for my rc plane and rocket! It will track velocity, distance, time, acceleration, gps, have a buzzer and a servo module to release a parachute on apogee!!

I created this for my school club as well, where we test out rc planes and would love to add this addition and teach the cub how to make a pcb. 

I first started with an idea and a name sky logger. I'v always thought about creating pcbs but thought they were to intercate and difficult. I learned that the best way to learn is to do, so instead of watching a youtube video I went right into it, were I succesfully created this amazing pcb, my first ever. I first started with a list of parts that I will probably use. This consisted of a gps, buzzer, led, distance and velocity tracker, esp32 Pico and more. 


S
## PCB images!!!!
![Skylog PCB](PCB%20FRONT.png)
![Skylog PCB back with art](PCB%20back%20plate%20with%20art.png)
![Skylog PCB](PCB.png)
![Skylog PCB](Startofpcb.png)








## Cost (AliExpress order)

| Name | Quantity | Unit Price (USD) | Total (USD) | Price (AED) | Link | Notes |
|---|---:|---:|---:|---:|---|---|
| Raspberry Pi Pico (RP2040, with headers) | 1 | 16.17 | 16.17 | 59.38 | [AliExpress](https://www.aliexpress.com/item/1005008058623788.html) | Main controller (A1) |
| GPS module GY-NEO6MV2 | 1 | 12.62 | 12.62 | 46.34 | [AliExpress](https://www.aliexpress.com/item/1005006153090346.html) | Position logging, plane only |
| W25Q64JVSSIQ SPI flash, SOIC-8 | 1 | 6.73 | 6.73 | 24.71 | [AliExpress](https://www.aliexpress.com/item/1005011573616561.html) | Flight data storage (U1); pack of 5 |
| Active buzzer TMB12A | 1 | 2.54 | 2.54 | 9.31 | [AliExpress](https://www.aliexpress.com/item/1005013110978481.html) | Recovery beeper (via Q1); pack of 10 |
| 1N5819HW Schottky diode, SOD-123 | 1 | 2.49 | 2.49 | 9.16 | [AliExpress](https://www.aliexpress.com/item/1005009499190440.html) | Power protection (D1); pack of 50 |
| Ceramic capacitor 100nF | 1 | 2.71 | 2.71 | 9.96 | [AliExpress](https://www.aliexpress.com/item/1005011747293156.html) | Decoupling (C2, C3); pack of 100 |
| Electrolytic capacitor 100uF | 1 | 2.02 | 2.02 | 7.42 | [AliExpress](https://www.aliexpress.com/item/1005011811368397.html) | Power smoothing (C1) |
| 2N7002 MOSFET, SOT-23 | 1 | 2.18 | 2.18 | 8.01 | [AliExpress](https://www.aliexpress.com/item/1005010446312149.html) | Buzzer switch (Q1); pack of 50 |
| SS12D00G4 slide switch | 1 | 2.32 | 2.32 | 8.52 | [AliExpress](https://www.aliexpress.com/item/1005012453860112.html) | Power switch (SW1); pack of 20 |
| BMP280 pressure sensor module 3.3V | 1 | 1.98 | 1.98 | 7.26 | [AliExpress](https://www.aliexpress.com/item/1005007306812689.html) | Altitude (J1) |
| GY-521 MPU6050 IMU module | 1 | 1.75 | 1.75 | 6.43 | [AliExpress](https://www.aliexpress.com/item/1005007989748804.html) | Motion sensing (J3) |
| Female pin header 2.54mm 1x__ | 1 | 2.19 | 2.19 | 8.06 | [AliExpress](https://www.aliexpress.com/item/1005012352493805.html) | Sensor and module sockets; pack of 10 |
| Female pin header 2.54mm 1x__ | 1 | 1.13 | 1.13 | 4.16 | [AliExpress](https://www.aliexpress.com/item/1005012352493805.html) | Sensor and module sockets; pack of 10 |
| Female pin header 2.54mm 1x__ | 1 | 2.14 | 2.14 | 7.85 | [AliExpress](https://www.aliexpress.com/item/1005012352493805.html) | Sensor and module sockets; pack of 10 |
| Female pin header 2.54mm 1x20 | 1 | 1.51 | 1.51 | 5.56 | [AliExpress](https://www.aliexpress.com/item/1005012940352449.html) | Pico sockets (A1); pack of 10 |
| Jumper shunt 2.54mm | 1 | 1.32 | 1.32 | 4.84 | [AliExpress](https://www.aliexpress.com/item/1005010500957186.html) | Mode jumper (J7); pack of 100 |
| Shipping | 1 | 6.74 | 6.74 | 24.77 |  | AliExpress shipping |
| Other (tax / fees) | 1 | 0.27 | 0.27 | 0.98 |  | Difference to order total |


   Full BOM with prices: [bom/bom.csv](Bom/bom.csv)
   




