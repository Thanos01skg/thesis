<div align="center">

  <h1>🏭 Industrial IoT Sensor Simulation</h1>
  
  <p>
    <b>A Python Simulation Script for Generating & Transmitting Industrial Sensor Data.</b>
  </p>

  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge" />
  <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" alt="Django Rest Framework Badge" />
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite Badge" />
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code Badge" />

  <br />
  <br />
</div>

---

## 1️⃣ Part 1: Python Simulation (Devices & Signals)

The core of this project is a robust Python script designed to simulate a real-world Industrial IoT environment. It acts as the "Client" in our architecture, generating environmental data and transmitting it to the Django server via HTTP requests.

### 🧠 System Architecture & Logic
The simulation is built using **Object-Oriented Programming (OOP)** to ensure modularity and scalability. The code consists of two primary classes:

#### A. `class HTTP_request`
This base class handles the networking layer. It is responsible for establishing communication with the Django REST API.
* **Device Registration**: Uses the `create_device()` method to register a new sensor on the server via a `POST` request to the `/devices/` endpoint. It retrieves and stores the unique `device_id` assigned by the database.
* **Signal Transmission**: Uses the `send_signal()` method to package the measurement data into a JSON payload and send it to the `/signals/` endpoint.

#### B. `class Sensor(HTTP_request)`
This class inherits from `HTTP_request` and represents the physical hardware.
* **Simulation Logic**: It takes `min` and `max` parameters to define the operating range of the sensor.
* **Data Generation**: The `generate_random_signals()` method produces a random float value (rounded to 2 decimals) within the specified range to simulate real-time fluctuations.
* **Timezone Awareness**: Utilizes the `pytz` library to attach an accurate timestamp (`Europe/Athens`) to every reading before sending it.

### 🔄 Execution Flow
When the script (`__main__`) is executed, it initializes the following virtual hardware setup:

1.  **Instantiation**: Creates 4 distinct sensors:
    * 3x Temperature Sensors (monitoring ranges: 20-30°C, 32-40°C, 28-32°C).
    * 1x Humidity Sensor (monitoring range: 1-3%).
2.  **Continuous Loop**: The system enters an infinite `while True` loop.
3.  **Interval**: Every **5 seconds**, it triggers all sensors to generate new data and push it to the server.

This automated process mimics the continuous stream of data found in industrial safety and monitoring systems, allowing for real-time decision-making.

---

## 2️⃣ Part 2: Visualization & Administration (AdminLTE)

To provide a professional, industrial-grade user interface, this project integrates **Django AdminLTE 3**. This modern UI wrapper enhances the default Django administration panel, offering a responsive dashboard for managing IoT devices and monitoring signals.

### 🛠️ Setup & Configuration

#### 1. Installing AdminLTE
The interface is powered by the `django-adminlte-3` package. This allows for a clean, side-menu navigation structure suitable for control room dashboards.

```bash
pip install django-adminlte-3
```

#### 2. Access Control (Superuser)
To access the dashboard, an administrator account is required. We create a superuser via the command line to gain full control over the application.

```bash
python manage.py createsuperuser
```

---

🎛️ The Dashboard Interface
Once logged in at `http://127.0.0.1:8000/admin/`, the system provides two main management modules under the Myapp section:

A. Device Management (`/devices/`)
This panel allows the operator to view and manage all registered IoT sensors.

List View: Displays active sensors like `HumidityS_ID_1`, `TempS_ID_2`, etc..

Actions: Supports searching, adding new devices manually, or deleting obsolete ones via dropdown actions.

B. Signal Management (`/signals/`)
This view provides a log of all incoming data packets.

Data Integrity: Allows admins to inspect specific signal values and types (e.g., verifying a temperature spike).

CRUD Operations: Signals can be edited or removed if data cleansing is required.
