# Project Aether-Link: Satellite-to-UAV Communication Modeling

### **Project Overview**
Hi! This is **Project Aether-Link**. As an Electrical Engineering (EEIT) student at OVGU, I wanted to explore a real-world challenge: keeping a drone connected when it’s flying far beyond the reach of traditional ground-based Wi-Fi or 5G. 

This project simulates a communication bridge between a **Low Earth Orbit (LEO)** satellite and a mobile drone terminal. I focused specifically on how the signal behaves in a "worst-case" scenario—modeling a typical rainy day in **Magdeburg, Germany**—to see if the connection would actually hold up for critical flight data.

---

### **Why I Built This**
The drone industry is rapidly moving toward **BVLOS (Beyond Visual Line of Sight)** operations. For long-distance deliveries or industrial inspections, drones need a space-based relay. This project is my technical deep dive into:
* **Path Loss:** Calculating signal attenuation over 550km of space.
* **Frequency Selection:** Why **Ku-Band (12 GHz)** is the industry choice for high-speed data.
* **Reliability:** Building a "Link Budget" that accounts for atmospheric interference.

---

### **The Technical Specs**
I've modeled the system using the following engineering parameters:
* **Orbit Altitude:** 550 km (Standard LEO).
* **Frequency:** 12.0 GHz (Ku-Band).
* **Weather Factors:** Included specific loss values for rain, clouds, and fog.
* **Target SNR:** Aiming for a minimum of **8 dB** to ensure stable QPSK data.

---

### **Current Progress: 40% Complete**
- [x] Phase 1: System Definition & LEO Parameters.
- [x] Phase 2: Core Link Budget Mathematics.
- [x] Phase 3: Atmospheric & Weather Fade Modeling.
- [ ] Phase 4: Dynamic Flight Simulation (In Progress).
- [ ] Phase 5: Autonomous Fail-safe Logic.

---

### **How to Use It**
I kept the code straightforward and modular so it’s easy for other engineers to verify. 
1. Ensure you have **Python 3.x** installed.
2. Clone this repository.
3. Run the primary analysis script: 
   ```bash
   python link_budget_calculator.py
   python flight_simulation.py
