"""
pip install gpiozero
"""

from gpiozero import DistanceSensor, Buzzer
import time

sensor = DistanceSensor(23, 24)
buz = Buzzer(17)

while True:
    print(f'Distance sensor to nearest object is {sensor.distance} m.')

    dist = sensor.distance
    buz.on()
    time.sleep(dist)
    
    buz.off()
    time.sleep(dist)