from adafruit_clue import clue
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

import time
import adafruit_ble_broadcastnet


clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(title="CLUE Sensor Data!", title_scale=2)

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

ble.start_advertising(advertisement)

print("This is BroadcastNet CLUE sensor:", adafruit_ble_broadcastnet.device_address)

while True:
    measurement = adafruit_ble_broadcastnet.AdafruitSensorMeasurement()


    clue_data[0].text = "Acceleration: {:.2f} {:.2f} {:.2f}".format(*clue.acceleration)
    clue_data[1].text = "Gyro: {:.2f} {:.2f} {:.2f}".format(*clue.gyro)
    clue_data[2].text = "Temperature: {:.1f}C".format(clue.temperature)
    clue_data[3].text = "Humidity: {:.1f}%".format(clue.humidity)
    measurement = clue.shake(shake_threshold=15, avg_count=10, total_delay=0.1)
    if clue.shake(shake_threshold=15, avg_count=10, total_delay=0.1):
        clue_data[4].text = "Shake: TRUE"
        clue.start_tone(523)
        #send signal to raspberry pie
        adafruit_ble_broadcastnet.broadcast(measurement)
        time.sleep(10)

    else:
        clue_data[4].text = "Shake: FALSE"
        clue.stop_tone()
    clue_data.show()

