import pandas as pd
import matplotlib.pyplot as plt

# Load the generated sensor data
data = pd.read_csv("equipment_sensor_data.csv")

# Define safe operating limits (industry-inspired values)
TEMP_LIMIT = 80        # °C
PRESSURE_LOW = 1.0     # bar
PRESSURE_HIGH = 1.4    # bar
VIBRATION_LIMIT = 0.6  # mm/s

# Fault detection logic
data["Temp_Alert"] = data["Temperature_C"] > TEMP_LIMIT
data["Pressure_Alert"] = (
    (data["Pressure_bar"] < PRESSURE_LOW) |
    (data["Pressure_bar"] > PRESSURE_HIGH)
)
data["Vibration_Alert"] = data["Vibration_mm_s"] > VIBRATION_LIMIT

# Overall equipment health flag
data["Equipment_Health_Flag"] = (
    data["Temp_Alert"] |
    data["Pressure_Alert"] |
    data["Vibration_Alert"]
)

# Summary results
total_faults = data["Equipment_Health_Flag"].sum()
print(f"Total abnormal readings detected: {total_faults}")

# --------- Visualization ---------

# Temperature trend
plt.figure()
plt.plot(data["Temperature_C"])
plt.axhline(TEMP_LIMIT)
plt.title("Equipment Temperature Trend")
plt.xlabel("Sample Index")
plt.ylabel("Temperature (°C)")
plt.show()

# Pressure trend
plt.figure()
plt.plot(data["Pressure_bar"])
plt.axhline(PRESSURE_LOW)
plt.axhline(PRESSURE_HIGH)
plt.title("Equipment Pressure Trend")
plt.xlabel("Sample Index")
plt.ylabel("Pressure (bar)")
plt.show()

# Vibration trend
plt.figure()
plt.plot(data["Vibration_mm_s"])
plt.axhline(VIBRATION_LIMIT)
plt.title("Equipment Vibration Trend")
plt.xlabel("Sample Index")
plt.ylabel("Vibration (mm/s)")
plt.show()
