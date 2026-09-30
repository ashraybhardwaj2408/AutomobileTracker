class ServiceTracker:
    def __init__(self, db):
        self.db = db

    def add_service_task(self, vehicle_id, service_name, interval_km, last_serviced_at):
        self.db.execute_query(
            "INSERT INTO service_logs (vehicle_id, service_name, interval_km, last_serviced_at) VALUES (?, ?, ?, ?)",
            (vehicle_id, service_name, interval_km, last_serviced_at)
        )
        print(f"Service task '{service_name}' added successfully.")

    def check_alerts(self, vehicle_id, current_odometer):
        tasks = self.db.fetch_all(
            "SELECT service_name, interval_km, last_serviced_at FROM service_logs WHERE vehicle_id = ?",
            (vehicle_id,)
        )
        print("\n--- Maintenance Status & Alerts ---")
        for name, interval, last_serviced in tasks:
            next_due = last_serviced + interval
            km_left = next_due - current_odometer
            if km_left <= 0:
                print(f"[ALERT] '{name}' is OVERDUE by {abs(km_left)} km! (Due at {next_due} km)")
            else:
                print(f"[OK] '{name}' is due in {km_left} km (At {next_due} km)")