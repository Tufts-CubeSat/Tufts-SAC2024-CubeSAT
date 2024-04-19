# SPDX-FileCopyrightText: 2019 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_lps35hw

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

try:
    lps = adafruit_lps35hw.LPS35HW(i2c)
    sensor_connected = True
except (ValueError, RuntimeError):
    sensor_connected = False
    print("LPS35HW sensor not detected.")


log_file = "pressuresensor_data.log"  # Name of the log file
with open(log_file, "a") as f:
                f.write("\nTUFTS CUBESAT SPACEPORT AMERICA CUP 2024\n")

while True:
    if sensor_connected:
        try:
            pressure = lps.pressure
            temperature = lps.temperature
            with open(log_file, "a") as f:
                f.write(f"Pressure: {pressure:.2f} hPa, Temperature: {temperature:.2f} C\n")
            print("Pressure: %.2f hPa" % pressure)
            print("Temperature: %.2f C" % temperature)
            print("")
        except (ValueError, RuntimeError):
            print("Error reading sensor data.")
    else:
        print("Sensor not connected.")

    time.sleep(1)

