import random
import time
import requests 
import json 
from datetime import datetime
import pytz

class HTTP_request:
    def __init__(self,url,name):
        self.name=name
        self.BASE_URL=url
        self.device_id = None

    def create_device(self): 
        url = f"{self.BASE_URL}devices/" 
        payload = {                 
            "name": self.name
        }
        headers = {                 
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers) 
        if response.status_code == 201: 
            data = response.json()
            self.device_id = data['id']
            print("Device created successfully:", data)
        else:
            print("Failed to create device:", response.status_code, response.text)
    
    def send_signal(self, value, signal_type="temperature"):  
        if self.device_id is None:
            print("No device ID found. Cannot send signal.")
            return
        
        url = f"{self.BASE_URL}signals/"                  
        payload = {                                                      
            "device": self.device_id,       
            "value": value,
            "signal_type": signal_type
        }
        headers = {                 
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers) 
        if response.status_code == 201:             
            print("Signal sent successfully:", response.json())
        else:
            print("Failed to send signal:", response.status_code, response.text)

class Sensor(HTTP_request): 
    def __init__(self,url,name,min,max): 
        super().__init__(url,name) 
        self.create_device() 
        self.name=name
        self.min=min
        self.max=max
  
    def generate_random_signals(self):
            self.SensorSignal = round(random.uniform(self.min,self.max),2) 
            greece_tz = pytz.timezone('Europe/Athens')
            timestamp = datetime.now(greece_tz).strftime("%Y-%m-%d %H:%M:%S") 
            print(f"[{timestamp}] {self.name} reading: {self.SensorSignal}") 
            self.send_signal(self.SensorSignal) 
            return self.SensorSignal
    
        
if __name__ == "__main__":
    BASE_URL = 'http://127.0.0.1:8000/api/' 

    temp_sensor1=Sensor(BASE_URL,"TempS_ID_1",20,30)
    temp_sensor2=Sensor(BASE_URL,"TempS_ID_2",32,40)
    temp_sensor3=Sensor(BASE_URL,"TempS_ID_3",28,32)
    hum_sensor=Sensor(BASE_URL,"HumidityS_ID_1",1,3)    

    while True:
        temp_sensor1.generate_random_signals()
        temp_sensor2.generate_random_signals()
        temp_sensor3.generate_random_signals()
        hum_sensor.generate_random_signals()
        time.sleep(5)