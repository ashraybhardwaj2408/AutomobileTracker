def validate_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def validate_odometer(prompt: str, min_value: float = 0.0) -> float:
    while True:
        value = validate_positive_float(prompt)
        if value < min_value:
            print(f"Error: Odometer reading cannot be less than the previous reading ({min_value}).")
            continue
        return value