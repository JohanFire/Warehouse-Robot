"""
script that checks json database content every second
"""

import json
import time

json_path = 'database.json'

def load_json():
    with open(json_path, 'r') as file:
        return json.load(file)

while True:
    current_value = load_json()['instruction']
    
    if current_value == True:
        print(f'current_value: {current_value} !!!')
        # gpio pin will be high
    elif current_value == False:
        print(f'current_value: {current_value} :(')
        # gpio pin will be low
        
    time.sleep(1)