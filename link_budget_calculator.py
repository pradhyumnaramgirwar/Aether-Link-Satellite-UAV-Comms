# Project Aether-Link: Phase 1-4 Complete Analysis
# Developed by: Pradhyumna Avinash Ramgirwar
import math

# --- 1. System Inputs ---
freq_ghz = 12.0       # Ku-Band
dist_km = 550.0       # LEO Altitude
p_tx_dbw = 10.0       # 10W Transmit Power
g_tx_dbi = 40.0       # Satellite Antenna Gain
g_rx_dbi = 5.0        # Drone Antenna Gain

# --- 2. Calculations ---
# Free Space Path Loss (FSPL)
fspl = 20 * math.log10(dist_km) + 20 * math.log10(freq_ghz) + 92.45

# Weather & Atmospheric Losses
loss_rain = 3.5
loss_clouds = 0.8
loss_gas = 0.2
total_loss = fspl + loss_rain + loss_clouds + loss_gas

# Final Received Power (Pr)
p_rx = (p_tx_dbw + g_tx_dbi + g_rx_dbi) - total_loss

# Signal-to-Noise Ratio (SNR)
noise_floor = -127.0
snr = p_rx - noise_floor

# --- 3. Output Report ---
print("-" * 30)
print("PROJECT AETHER-LINK REPORT")
print("-" * 30)
print(f"Path Loss:       {round(fspl, 2)} dB")
print(f"Total Loss:      {round(total_loss, 2)} dB (incl. Weather)")
print(f"Received Power:  {round(p_rx, 2)} dBW")
print(f"Final SNR:       {round(snr, 2)} dB")
print("-" * 30)

if snr >= 8.0:
    print("STATUS: SUCCESS - Link is Stable")
else:
    print("STATUS: FAIL - Signal too weak")