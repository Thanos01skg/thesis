## 🐍 IoT Sensor Simulator (Python Script)

This Python script acts as a **virtual sensor network** designed to simulate real-time environmental data collection. It automates the generation and transmission of temperature and humidity readings to a centralized API.

### 🎯 Core Logic & Functionality

* **Automated Device Creation**: Upon execution, the script automatically registers new virtual devices (sensors) with the backend API via HTTP POST requests.
* **Randomized Data Generation**: It simulates realistic environmental fluctuations by generating random decimal values within predefined ranges (e.g., 20°C–30°C for temperature).
* **Precise Localization**: Every reading is timestamped using the `pytz` library to ensure accurate logging according to the **Europe/Athens** timezone.
* **Continuous Monitoring Loop**: The script operates in an infinite loop, sending fresh data from all sensors every **5 seconds** to maintain a live data stream.

### 🛠️ Technical Implementation

* **OOP Architecture**: Built using Object-Oriented Programming, featuring a base `HTTP_request` class for API communication and a specialized `Sensor` class for data logic.
* **Integration**: Specifically designed to work with a **Django REST Framework** backend, targeting the `/api/signals/` endpoint.
* **Robust Communication**: Uses the `requests` library to handle JSON payloads and manages HTTP status codes to verify successful data delivery.

### 📊 Simulation Parameters
The script initializes four distinct virtual sensors:
1. **TempS_ID_1**: 20°C - 30°C
2. **TempS_ID_2**: 32°C - 40°C
3. **TempS_ID_3**: 28°C - 32°C
4. **HumidityS_ID_1**: 1% - 3% (Standard deviation)


---


### 🔗 Source Code
You can explore the full Python Script here:
* 📄 [**View Python Script**](./IotSignalGenerator.py)
