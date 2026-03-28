# Project Aether-Link: Phase 5 - Autonomous Fail-safe Logic
# Purpose: Simulating a real-time signal monitor that triggers emergency protocols.

import time

# Thresholds for a Master's Level Project
CRITICAL_SNR = 5.0  # Below this, the drone loses control
WARNING_SNR = 7.0   # Below this, we should alert the pilot

# Simulated live signal readings (simulating a drone flying into a storm)
signal_readings = [8.6, 8.2, 7.5, 6.8, 5.5, 4.8, 4.2]

print("--- AETHER-LINK LIVE SIGNAL MONITOR ---")
print("Starting Satellite Handshake...")
time.sleep(1)

for snr in signal_readings:
    print(f"Current SNR: {snr} dB", end=" -> ")
    
    if snr > WARNING_SNR:
        print("STATUS: LINK STABLE")
    elif snr <= WARNING_SNR and snr > CRITICAL_SNR:
        print("STATUS: WARNING - DEGRADED SIGNAL")
    else:
        print("STATUS: CRITICAL! TRIGGERING AUTO-RTH (Return to Home)")
        print("Action: Engaging Satellite Fail-safe...")
        break # Stop the simulation once we hit emergency mode
    
    time.sleep(0.5) # Makes it feel like a real-time monitor

print("---------------------------------------")
print("Simulation Ended.")