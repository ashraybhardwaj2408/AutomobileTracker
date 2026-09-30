from models.vehicle_specs import get_vehicle_specs

class VehicleManager:
    def __init__(self, db):
        self.db = db

    def add_vehicle(self, make, model, year, initial_odometer):
        self.db.execute_query(
            "INSERT INTO vehicles (make, model, year, current_odometer) VALUES (?, ?, ?, ?)",
            (make, model, year, initial_odometer)
        )
        print(f"Successfully added {year} {make} {model}!")

    def list_vehicles(self):
        return self.db.fetch_all("SELECT id, make, model, year, current_odometer FROM vehicles")

    def get_vehicle(self, vehicle_id):
        return self.db.fetch_one("SELECT id, make, model, year, current_odometer FROM vehicles WHERE id = ?", (vehicle_id,))
    
    def update_odometer(self, vehicle_id, new_odometer):
        self.db.execute_query("UPDATE vehicles SET current_odometer = ? WHERE id = ?", (new_odometer, vehicle_id))

    def display_vehicle_profile(self, vehicle_id):
        v = self.get_vehicle(vehicle_id)
        if not v:
            print("Vehicle not found.")
            return
        
        v_id, make, model, year, odometer = v
        print(f"\n========================================")
        print(f" VEHICLE PROFILE: {year} {make} {model}")
        print(f"========================================")
        print(f" Current Odometer : {odometer} km")
        
        matched_key, specs = get_vehicle_specs(model)
        if specs:
            print(f"\n --- Factory Specifications ({matched_key}) ---")
            print(f" • Vehicle Type : {specs['type']}")
            print(f" • Engine Size  : {specs['engine']}")
            print(f" • Max Power    : {specs['power']}")
            print(f" • Max Torque   : {specs['torque']}")
            print(f" • Fuel Tank    : {specs['tank']}")
            print(f" • Est. Mileage : {specs['avg_efficiency']}")
        else:
            print("\n [Note: Custom or rare model. Factory specs not in database yet.]")
        print(f"========================================")