class FuelTracker:
    def __init__(self, db):
        self.db = db

    def add_fuel_log(self, vehicle_id, odometer, litres, cost):
        #insert log
        self.db.execute_query(
            "INSERT INTO fuel_logs (vehicle_id, odometer, litres, cost) VALUES (?, ?, ?, ?)",
            (vehicle_id, odometer, litres, cost)
        )
        #update vehicle current odometer
        self.db.execute_query("UPDATE vehicles SET current_odometer = ? WHERE id = ?", (odometer, vehicle_id))
        print("Fuel log added successfully and vehicle odometer updated.")

    def calculate_efficiency(self, vehicle_id):
        logs = self.db.fetch_all(
            "SELECT odometer, litres FROM fuel_logs WHERE vehicle_id = ? ORDER BY odometer ASC",
            (vehicle_id,)
        )
        if len(logs) < 2:
            print("Need at least 2 fuel logs to calculate fuel economy.")
            return

        print("\n--- Fuel Efficiency History ---")
        for i in range(1, len(logs)):
            prev_odometer, _ = logs[i - 1]
            curr_odometer, curr_litres = logs[i]
            distance = curr_odometer - prev_odometer
            if curr_litres > 0:
                economy = distance / curr_litres
                print(f"Trip {i}: Distance Covered: {distance} km | Fuel Used: {curr_litres} L | Efficiency: {economy:.2f} km/L")