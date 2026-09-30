DATABASE_SPECS = {
    "Honda CB350": {
        "type": "Motorcycle", "engine": "348 cc", "power": "21.07 bhp", 
        "torque": "30 Nm", "tank": "15 Litres", "avg_efficiency": "35 km/L"
    },
    "Suzuki Access 125": {
        "type": "Scooter", "engine": "124 cc", "power": "8.7 bhp", 
        "torque": "10 Nm", "tank": "5 Litres", "avg_efficiency": "45 km/L"
    },
    "Royal Enfield Guerrilla 450": {
        "type": "Motorcycle", "engine": "452 cc", "power": "39.47 bhp", 
        "torque": "40 Nm", "tank": "11 Litres", "avg_efficiency": "28 km/L"
    },
    "Bajaj Pulsar NS400Z": {
        "type": "Motorcycle", "engine": "373 cc", "power": "39.4 bhp", 
        "torque": "35 Nm", "tank": "12 Litres", "avg_efficiency": "30 km/L"
    },
    "Tata Nexon": {
        "type": "Compact SUV", "engine": "1.2L Turbo Petrol / 1.5L Diesel", "power": "118 bhp", 
        "torque": "170 Nm", "tank": "44 Litres", "avg_efficiency": "17 km/L"
    },
    "Skoda Slavia": {
        "type": "Sedan", "engine": "1.0L / 1.5L TSI", "power": "114 / 148 bhp", 
        "torque": "178 / 250 Nm", "tank": "45 Litres", "avg_efficiency": "18 km/L"
    },
    "Mahindra Thar": {
        "type": "Off-road SUV", "engine": "2.0L Stallion / 2.2L mHawk", "power": "150 bhp", 
        "torque": "320 Nm", "tank": "57 Litres", "avg_efficiency": "12 km/L"
    }
}

def get_vehicle_specs(model_name: str):
    for key, specs in DATABASE_SPECS.items():
        if model_name.lower() in key.lower():
            return key, specs
    return None, None 