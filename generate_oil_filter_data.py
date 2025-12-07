import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_synthetic_oil_filter_data(n_rows=2000):
    vehicle_types = ["SUV", "Sedan", "Hatchback", "LCV", "Truck", "Bus"]
    road_types = ["city", "highway", "offroad", "mixed"]
    load_types = ["light", "medium", "heavy"]
    fuel_types = ["Petrol", "Diesel", "CNG"]
    driving_styles = ["calm", "normal", "aggressive"]

    # Target classes
    condition_labels = ["Green", "Light-Green", "Yellow", "Orange", "Dark-Orange", "Red"]

    data = []

    for _ in range(n_rows):
        vehicle_type = random.choice(vehicle_types)
        engine_capacity = random.randint(1200, 8000)

        # Generate dates
        current_date = datetime(2024, random.randint(1, 12), random.randint(1, 28))
        days_old = random.randint(0, 400)
        change_date = current_date - timedelta(days=days_old)

        km_after_change = int(days_old * random.uniform(10, 200))

        road = random.choice(road_types)
        load = random.choice(load_types)

        temp = random.uniform(70, 130)
        viscosity = random.uniform(20, 100)
        rpm = random.randint(1200, 4000)
        idle_pct = random.randint(5, 40)
        ambient = random.uniform(10, 45)
        fuel = random.choice(fuel_types)
        driving = random.choice(driving_styles)

        # Label assignment based on age
        if days_old <= 30:
            label = "Green"
        elif days_old <= 90:
            label = "Light-Green"
        elif days_old <= 180:
            label = "Yellow"
        elif days_old <= 270:
            label = "Orange"
        elif days_old <= 330:
            label = "Dark-Orange"
        else:
            label = "Red"

        # Stress adjustments
        stress = 0

        if load == "heavy":
            stress += 1
        if road == "offroad":
            stress += 1
        if temp > 110:
            stress += 1
        if viscosity < 40:
            stress += 1
        if rpm > 3000:
            stress += 1
        if driving == "aggressive":
            stress += 1

        # Upgrade severity if stress is high
        index = condition_labels.index(label)
        index = min(index + (stress // 3), len(condition_labels) - 1)
        final_label = condition_labels[index]

        data.append([
            vehicle_type, engine_capacity, change_date.date(), current_date.date(),
            days_old, km_after_change, road, load, temp, viscosity, rpm,
            idle_pct, ambient, fuel, driving, final_label
        ])

    df = pd.DataFrame(data, columns=[
        "vehicle_type", "engine_capacity_cc", "oil_filter_change_date",
        "current_date", "oil_filter_age_days", "km_after_change",
        "road_type", "load_type", "avg_oil_temperature", "oil_viscosity_index",
        "engine_rpm_avg", "idling_percentage", "ambient_temperature",
        "fuel_type", "driving_style", "oil_filter_condition"
    ])

    return df


# Example: generate 2000 rows and save CSV
df = generate_synthetic_oil_filter_data(2000)
df.to_csv("oil_filter_dataset_2000.csv", index=False)
print("Synthetic dataset (2000 rows) generated successfully!")
