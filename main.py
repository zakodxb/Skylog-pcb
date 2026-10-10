# Skylog flight logger - bring-up test
# MicroPython for Raspberry Pi Pico (RP2040)
#
# AI DISCLOSURE: this file was written with AI assistance (Claude, by Anthropic).
# STATUS: NOT YET TESTED on hardware - the PCB has not been assembled yet.
#
# What it does when the board is powered:
#   1. Beeps the buzzer once and blinks the LED
#   2. Scans the I2C bus and reports whether the BMP280 and MPU6050 answer
#   3. Reads the flash chip's ID to confirm the W25Q64JV is soldered correctly
#   4. Loops: blinks the LED, prints battery voltage and the J7 jumper state

from machine import Pin, I2C, SPI, ADC
import time

# ---- Pin map (from the Skylog schematic) ----
LED_PIN = 12      # D2 status LED
BUZZER_PIN = 11   # gate of Q1 (2N7002); HIGH = buzzer on
MODE_PIN = 13     # J7 mode jumper
BATT_ADC_PIN = 26 # battery voltage divider
I2C_SDA, I2C_SCL = 4, 5
FLASH_SCK, FLASH_MOSI, FLASH_MISO, FLASH_CS = 18, 19, 16, 17

# Battery divider ratio. 2.0 assumes two equal resistors (R4/R5 = 100k each).
# Change this if your schematic differs.
BATT_DIVIDER = 2.0

led = Pin(LED_PIN, Pin.OUT)
buzzer = Pin(BUZZER_PIN, Pin.OUT, value=0)
mode = Pin(MODE_PIN, Pin.IN, Pin.PULL_UP)   # jumper fitted = pin pulled low
batt = ADC(BATT_ADC_PIN)

i2c = I2C(0, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL), freq=400_000)
spi = SPI(0, baudrate=1_000_000, polarity=0, phase=0,
          sck=Pin(FLASH_SCK), mosi=Pin(FLASH_MOSI), miso=Pin(FLASH_MISO))
flash_cs = Pin(FLASH_CS, Pin.OUT, value=1)

KNOWN_I2C = {
    0x76: "BMP280",
    0x77: "BMP280 (alternate address)",
    0x68: "MPU6050",
    0x69: "MPU6050 (alternate address)",
}


def beep(seconds=0.15):
    buzzer.value(1)
    time.sleep(seconds)
    buzzer.value(0)


def scan_i2c():
    found = i2c.scan()
    if not found:
        print("I2C: nothing found - check J1/J3 solder joints and SDA/SCL")
        return
    for addr in found:
        print("I2C: 0x%02X  %s" % (addr, KNOWN_I2C.get(addr, "unknown device")))
    if not any(a in found for a in (0x76, 0x77)):
        print("I2C: BMP280 NOT found")
    if not any(a in found for a in (0x68, 0x69)):
        print("I2C: MPU6050 NOT found")


def check_flash():
    flash_cs.value(0)
    spi.write(b"\x9f")            # JEDEC ID command
    ident = spi.read(3)
    flash_cs.value(1)
    print("Flash ID:", ident.hex())
    if ident == b"\xef\x40\x17":
        print("Flash: W25Q64JV detected - OK")
    else:
        print("Flash: unexpected ID (expected ef4017) - check U1 soldering")


def battery_volts():
    raw = batt.read_u16()
    return raw / 65535 * 3.3 * BATT_DIVIDER


print("Skylog bring-up test")
beep()
led.value(1)
time.sleep(0.3)
led.value(0)
scan_i2c()
check_flash()

while True:
    led.toggle()
    jumper = "fitted" if mode.value() == 0 else "open"
    print("Battery: %.2f V   J7 jumper: %s" % (battery_volts(), jumper))
    time.sleep(1)
