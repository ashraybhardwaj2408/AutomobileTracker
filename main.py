from database.db_handler import DatabaseHandler
from models.vehicle import VehicleManager
from models.fuel_log import FuelTracker
from models.service_log import ServiceTracker
from utils.validators import validate_positive_float, validate_odometer

def main():
    db = DatabaseHandler()
    vehicles = VehicleManager(db)
    fuel_tracker = FuelTracker(db)
    service_tracker = ServiceTracker(db)

    while True:
        print("\n=== Personal Automotive Maintenance & Expense Tracker ===")
        print("1. Add New Vehicle")
        print("2. List Vehicles & View Spe6cs")
        print("3. Log Fuel Fill-up")
        print("4. View Fuel Efficiency")
        print("5. Add Maintenance Task")
        print("6. Check Service Alerts")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ").strip()

        if choice == '1':
            manufacturers = [
                "Honda", "Suzuki", "Toyota", "Tata", "Hyundai", 
                "Mahindra", "Jeep", "Ford", "Kia", "Royal Enfield", 
                "TVS", "KTM", "Bajaj", "Renault", "Hero", "Volkswagen", "Skoda"
            ]
            
            print("\n--- Select Manufacturer ---")
            for idx, brand in enumerate(manufacturers, 1):
                print(f"{idx}. {brand}")
            
            try:
                brand_choice = int(input("Enter choice number (1-17): "))
                if 1 <= brand_choice <= len(manufacturers):
                    make = manufacturers[brand_choice - 1]
                else:
                    print("Invalid selection. Defaulting to custom entry.")
                    make = input("Enter Make manually: ")
            except ValueError:
                make = input("Enter Make manually: ")

            model = input("Enter Model (e.g., CB350, Access 125, Nexon, Slavia): ")
            year = int(validate_positive_float("Enter Manufacturing Year: "))
            odometer = validate_positive_float("Enter Current Odometer Reading (km): ")
            vehicles.add_vehicle(make, model, year, odometer)

        elif choice == '2':
            v_list = vehicles.list_vehicles()
            if not v_list:
                print("No vehicles found.")
            else:
                print("\n--- Registered Vehicles ---")
                for v in v_list:
                    print(f"ID: {v[0]} | {v[3]} {v[1]} {v[2]} | Odometer: {v[4]} km")
                
                inspect_id = input("\nEnter Vehicle ID to view full profile & factory specs (or press Enter to skip): ").strip()
                if inspect_id.isdigit():
                    vehicles.display_vehicle_profile(int(inspect_id))

        elif choice == '3':
            v_id = int(validate_positive_float("Enter Vehicle ID: "))
            v_data = vehicles.get_vehicle(v_id)
            if not v_data:
                print("Vehicle not found.")
                continue
            current_odo = v_data[4]
            odometer = validate_odometer(f"Enter Current Odometer (Min {current_odo}): ", min_value=current_odo)
            litres = validate_positive_float("Enter Fuel Filled (Litres): ")
            cost = validate_positive_float("Enter Total Cost (Currency): ")
            fuel_tracker.add_fuel_log(v_id, odometer, litres, cost)

        elif choice == '4':
            v_id = int(validate_positive_float("Enter Vehicle ID: "))
            fuel_tracker.calculate_efficiency(v_id)

        elif choice == '5':
            v_id = int(validate_positive_float("Enter Vehicle ID: "))
            name = input("Enter Service Name (e.g., Oil Change, Chain Lube): ")
            interval = validate_positive_float("Enter Service Interval (km): ")
            last_serviced = validate_positive_float("Odometer reading when last serviced: ")
            service_tracker.add_service_task(v_id, name, interval, last_serviced)

        elif choice == '6':
            v_id = int(validate_positive_float("Enter Vehicle ID: "))
            v_data = vehicles.get_vehicle(v_id)
            if v_data:
                service_tracker.check_alerts(v_id, v_data[4])
            else:
                print("Vehicle not found.")

        elif choice == '7':
            db.close()
            print("Exiting tracker. Have a safe ride!")
            break
        else:
            print("Invalid choice. Please select between 1 and 7.")

if __name__ == "__main__":
    main()
    