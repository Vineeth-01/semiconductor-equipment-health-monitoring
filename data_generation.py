import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
samples = 500

# Simulated sensor data (normal operation)
temperature = np.random.normal(loc=65, scale=2, size=samples)
pressure = np.random.normal(loc=1.2, scale=0.05, size=samples)
vibration = np.random.normal(loc=0.3, scale=0.05, size=samples)

# Introduce abnormal behavior (equipment degradation)
temperature[400:] += np.random.normal(10, 2, 100)
vibration[420:] += np.random.normal(0.4, 0.1, 80)

# Create DataFrame
data = pd.DataFrame({
    "Temperature_C": temperature,
    "Pressure_bar": pressure,
    "Vibration_mm_s": vibration
})

# Save dataset
data.to_csv("equipment_sensor_data.csv", index=False)

print("Equipment sensor dataset generated successfully.")
