# LAM Research Challenge (logical league round) – Team Mahagatbandhan
## 🏆 Secured 2nd Position Nationwide among 1000+ Teams

> 🎥 **Our Presentation:**  

https://github.com/user-attachments/assets/2cbd09a7-4317-4391-9977-a51414e5e522




This repository contains the complete work, simulations, designs, and documentation developed by **Team Mahagatbandhan (IIT Delhi)** for the **LAM Research Challenge 2025**, where we proudly **secured 2nd place overall at the national level among 1000+ participating teams**.

---

# 📌 Project Overview
The challenge required designing an automated arena where a robot performs fluid transfer, object handling, LED indication, line-following navigation, gate-based event triggers, and obstacle detection.

We developed a complete hardware-in-simulation ecosystem including custom robots, control algorithms, and signal-based coordination.

---

# 🧩 1. Arena Circuit Development
The arena was designed as an event-driven automation system synchronized with the movement of the ALFR.

### Highlights
- **Gate 1:** Triggers fluid delivery (125 ml)  
- **Gate 2:** Activates glowing LAM LED  
- **LCD Status Display**  
- **Signal-based control** using `sim.setInt32Signal()` and `sim.getInt32Signal()`  

A water parcel moves along paths representing a peristaltic pump delivering 125 ml of fluid.

---

# 🤖 2. Single Arm Robot (SARM) – Omni-Wheel Platform
Custom-designed base and arm:

- Four omni wheels for high agility  
- Redesigned gripper with adjustable jaws  
- CAD → URDF → CoppeliaSim validation  
- Center-of-mass balanced for stability  

---

# 🚗 3. Advanced Line Follower Robot (ALFR)
Features:

- **5 Vision Sensors** for accurate line following  
- **1 Proximity Sensor** for obstacle detection  
- Dynamic motor control based on sensor inputs  
- Debugging UI included  

---

# 💧 4. Peristaltic Pump Simulation
Simulated water movement over dummy paths triggered by:

```
sim.getInt32Signal('trigger water release')
```

Represents a controlled transfer of 125 ml fluid.

---

# 🛠️ 5. Custom 3D Models
- Full CAD of SARM + Gripper  
- Custom ALFR chassis  
- URDF exports for both bots  

---

# ⏱️ 6. Simulation Statistics
- True simulation time: **2 minutes 43 seconds**  
- Recorded video: **8 minutes** (due to real-time factor)

---

# 🏆 Achievement
## 2nd Position in the LAM Research Challenge (Logical League Round) 2025  
### Among 1000+ teams across India

---

# 👥 Team
- **Shreyans Jain** — Mechanical Engineering(Team Leader)  
- **Dilshan** — Computer Science Engineering 
- **Sambhav Singh Aditya** — Computer Science Engineering  
- **Verchasv Garg** — Electrical Engineering  

---

# 📁 Repository Structure
```
📦 LAM-Research-Challenge
 ┣ 📁 CAD_Models
 ┣ 📁 URDF_Files
 ┣ 📁 CoppeliaSim_Scenes
 ┣ 📁 Lua_Scripts
 ┣ 📁 ALFR_Code
 ┣ 📁 SARM_Simulation
 ┣ 📁 Arena_System
 ┣ 📄 Logical_League_Documentation.pdf
 ┗ 📄 README.md
```

---

# 🚀 How to Run
1. Open CoppeliaSim  
2. Load the arena scene  
3. Ensure URDF files are correctly linked  
4. Run simulation  

---

# 📜 License
Open for educational and research usage.

