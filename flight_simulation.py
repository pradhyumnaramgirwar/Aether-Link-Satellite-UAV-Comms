# Project Aether-Link: Phase 4 - Dynamic Flight Simulation
# Purpose: Simulate SNR changes as the UAV moves across the satellite beam footprint.

import math

# --- 1. Baseline Data (From our successful Step 1) ---
baseline_snr = 8.66  # Our stable signal at the center (0 km)

print("-" * 50)
print("PROJECT AETHER-LINK: DYNAMIC FLIGHT SIMULATION")
print("-" * 50)
print(f"{'Distance (km)':<15} | {'Current SNR (dB)':<18} | {'Status'}")
print("-" * 50)

# --- 2. Movement Loop ---
# We simulate the drone flying from 0km to 40km away from the beam center
for distance in range(0, 45, 5):
    
    # Engineering Assumption: Signal drops by ~0.15 dB per km as we move off-axis
    off_axis_loss = distance * 0.15
    current_snr = baseline_snr - off_axis_loss
    
    # Determining Link Quality Logic
    if current_snr >= 7.5:
        link_quality = "EXCELLENT (HD Video Ready)"
    elif current_snr >= 6.0:
        link_quality = "GOOD (Telemetry Only)"
    elif current_snr >= 5.0:
        link_quality = "STABLE (Emergency Mode)"
    else:
        link_quality = "CRITICAL - SIGNAL DROPPED"

    # Print the flight log row
    print(f"{distance:<15} | {round(current_snr, 2):<18} | {link_quality}")

print("-" * 50)
print("Simulation Complete: Analysis of Beam Edge Performance.")