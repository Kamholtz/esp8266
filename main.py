

# class NodeMcu:

#     # ESP8266 allows software PWM in all I/O pins: GPIO0 to GPIO16. PWM signals on ESP8266 have 10-bit resolution
#     # The ESP8266 supports interrupts in any GPIO, except GPIO16.


#     # GPIO16: pin is high at BOOT
#     # eUsed for deep sleep
#     d0 = Pin(16)

#     # Usually used for I2C SCL
#     d1 = Pin(5)

#     # Usually used for I2C SDA
#     d2 = Pin(4)

#     # GPIO0: boot failure if pulled LOW
#     d3 = Pin(0)

#     # GPIO2: pin is high on BOOT, boot failure if pulled LOW
#     d4 = Pin(2)

#     # GPIO14: SCLK
#     d5 = Pin(14)

#     # GPIO12: MISO
#     d6 = Pin(12)

#     # GPIO13: MOSI
#     d7 = Pin(13)

#     # GPIO15: boot failure if pulled HIGH
#     # GPIO15: CS
#     d8 = Pin(15)

#     # GPIO3: pin is high at BOOT
#     rx = Pin(3)

#     # GPIO1: pin is high at BOOT, boot failure if pulled LOW
#     tx = Pin(1)

#     # GPIO10: pin is high at BOOT
#     sd3 = Pin(10)

#     # GPIO9: pin is high at BOOT
#     sd2 = Pin(9)

