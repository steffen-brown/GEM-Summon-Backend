# GEM Summoner Backend

[![UIUC ECE 484](https://img.shields.io/badge/Course-ECE%20484-orange)](https://ece.illinois.edu/)

Flask-based API for the **GEM Summoner** project, serving as the bridge between the web frontend and the vehicle’s ROS-based control system. It manages live GPS locations, summon targets, and vehicle status updates.

## Contribution
This project was fully authored and developed by Steffen Brown, including all code implementation, experimentation, and documentation.

## Features
- **Authentication** via a simple token-based system  
- **Phone location tracking** for summon target  
- **Car location tracking** for live vehicle position  
- **Car status management** (`IDLE`, `SUMMONING`, `ARRIVED`)  
- **CORS-enabled** for seamless communication with the React frontend  

## Related Repositories
This backend is one part of the complete GEM Summoner system. For vehicle firmware, ROS nodes, and system architecture, see:  
🔗 [GEM-Summon-Firmware](https://github.com/steffen-brown/GEM-Summon-Firmware)  

Frontend interface:  
🔗 [GEM-Summon-Frontend](https://github.com/steffen-brown/GEM-Summon-Frontend)  

## API Endpoints

### Authentication
- `POST /login` — Authenticate and receive access token  

### Phone Location
- `POST /location` — Update phone’s GPS location  
- `GET /latest-location` — Retrieve latest phone location  

### Car Location
- `POST /car-location` — Update car’s GPS location  
- `GET /latest-car-location` — Retrieve latest car location  

### Car Status
- `POST /car-status` — Update car status (`IDLE`, `SUMMONING`, `ARRIVED`)  
- `GET /latest-car-status` — Retrieve latest car status  

## Running Locally
```bash
pip install flask flask-cors
python app.py
