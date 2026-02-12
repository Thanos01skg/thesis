<div align="center">

  <h1>🏭 Industrial IoT Sensor Simulation</h1>
  
  <p>
    <b>A Web-based System for Managing Temperature & Humidity Data.</b>
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

## 📖 Overview
The goal of this project is to demonstrate the **collection, transmission, and management of sensor data** in real-time. It highlights the importance of automation in industrial monitoring by simulating:
* **Temperature Sensors**
* **Humidity Sensors**

This script acts as the "Client" side of the architecture, sending continuous streams of data to the central Django server.

---

## 🧠 Code Architecture
The simulation is built using Object-Oriented Programming (OOP) in Python, featuring two main classes as described in our documentation:

### 1. `class HTTP_request`
* **Role**: Manages the communication with the server.
* **Functionality**: Handles the device registration and sends `POST` requests to the Django REST API endpoints.

### 2. `class Sensor`
* **Role**: Represents the physical hardware.
* **Functionality**: 
    * Generates random measurement values within realistic ranges.
    * Uses the parent `HTTP_request` class to transmit these values as "Signals".

---

## 📡 Data Flow & Integration
This script is designed to feed data into a Django-based backend.

1.  **Data Generation**: The `Sensor` class creates a random data point.
2.  **Transmission**: The script packages this data into a JSON payload.
3.  **API Consumption**: Data is sent via HTTP to the Django REST API.
4.  **Visualization**: The data is then visualized in the backend's **AdminLTE** dashboard and Real-Time Graphs for decision-making.

---

## 🚀 Usage

To run the simulation, ensure your Django server is running first, then execute:

```bash
python sensor_simulation.py
