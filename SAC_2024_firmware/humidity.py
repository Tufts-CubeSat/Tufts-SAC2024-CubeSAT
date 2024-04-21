# SPDX-FileCopyrightText: 2019 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_shtc3

try:
	i2c = board.I2C()  # uses board.SCL and board.SDA
	# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
	sht = adafruit_shtc3.SHTC3(i2c)
except (ValueError, RuntimeError):
    sensor_connected = False
    print("SHTC3 sensor not detected.")


log_file = "humiditysensor_data.log"  # Name of the log file
with open(log_file, "a") as f:
                f.write("\nTUFTS CUBESAT SPACEPORT AMERICA CUP 2024\n")

while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    print("")
    time.sleep(1)

