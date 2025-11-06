import sim
import tkinter as tk
import math

sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID != -1:
    print("Connected to CoppeliaSim")
    revolute_handles = []
    for i in range(1, 6):
        _, handle = sim.simxGetObjectHandle(clientID, f'/SARM/joint_{i}', sim.simx_opmode_blocking)
        revolute_handles.append(handle)
    prismatic_handles = []
    for i in range(6, 8):
        _, handle = sim.simxGetObjectHandle(clientID, f'/SARM/joint_{i}', sim.simx_opmode_blocking)
        prismatic_handles.append(handle)
    root = tk.Tk()
    root.title("7-Joint Control (Legacy API)")
    rev_frame = tk.Frame(root)
    rev_frame.pack()
    def create_revolute_slider(joint_index):
        def update(val):
            angle = math.radians(float(val))
            sim.simxSetJointPosition(clientID, revolute_handles[joint_index], angle, sim.simx_opmode_oneshot)
        
        slider = tk.Scale(rev_frame, from_=-180, to=180, orient="vertical",
                          label=f"Joint {joint_index + 1}", command=update, length=300)
        slider.pack(side="left", padx=10)
    for i in range(5):
        create_revolute_slider(i)
    prism_frame = tk.Frame(root)
    prism_frame.pack(pady=20)
    def update_prismatic(val):
        position = (float(val)) / 1000.0 
        sim.simxSetJointPosition(clientID, prismatic_handles[0], position, sim.simx_opmode_oneshot)  
        sim.simxSetJointPosition(clientID, prismatic_handles[1], -position, sim.simx_opmode_oneshot) 
    prismatic_slider = tk.Scale(prism_frame, from_=0, to=100, orient="horizontal",
                                label="Prismatic Joints (6 & 7)", command=update_prismatic, length=300)
    prismatic_slider.pack()
    root.mainloop()
    sim.simxFinish(clientID)

else:
    print("Failed to connect to CoppeliaSim")
