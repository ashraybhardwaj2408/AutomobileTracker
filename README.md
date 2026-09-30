# Personal Automotive Maintenance & Expense Tracker

## 1. Project Title
Personal Automotive Maintenance & Expense Tracker

## 2. Overview of the Project
The Personal Automotive Maintenance & Expense Tracker is a modular, object-oriented Python command-line application designed to help vehicle owners manage their automobile and motorcycle fleets. Backed by a lightweight SQLite database, it provides a centralized platform to log fuel fill-ups, calculate ongoing fuel efficiency, monitor routine wear-and-tear service milestones, and instantly retrieve factory vehicle specifications.

## 3. Features
* **Fleet Management & Brand Selector:** Register and manage multiple cars, motorcycles, and scooters using an interactive brand selection menu.
* **Smart Factory Specifications Lookup:** Automatically retrieves technical parameters (engine displacement, power output, torque, fuel tank capacity, and estimated mileage) based on the specific vehicle model.
* **Fuel Economy Tracking:** Records fuel consumption logs and accurately calculates distance-based efficiency metrics ($\text{km/L}$).
* **Proactive Service Scheduler:** Monitors odometer readings to provide automated alerts for upcoming or overdue maintenance tasks (e.g., oil changes, chain lubrication).
* **Robust Input Validation:** Enforces strict error handling and positive-value checks to guarantee data integrity and prevent logical errors (like entering a lower odometer reading than the previous log).

## 4. Technologies/Tools Used
* **Programming Language:** Python 3.x
* **Database:** SQLite3 (Local persistent storage)
* **Version Control:** Git & GitHub
* **Development Environment:** Visual Studio Code (VS Code)

## 5. Steps to Install & Run the Project
1. **Clone the Repository:** Download or clone this project repository to your local machine.
2. **Open the Environment:** Open the `AutomobileTracker` project folder inside Visual Studio Code (VS Code).
3. **Verify Prerequisites:** Ensure Python 3 is installed on your system by opening a terminal and running:
   ```bash
   python --version
   ```
4. Launch the Application: Open the integrated terminal in VS Code, ensure you are in the root directory of the project, and execute the main controller script:
```Bash
python main.py
```

## 6. Instructions for TestingTest Vehicle Registration: 
* Run option 1 from the main menu, select a manufacturer from the predefined list, and enter the model, year, and starting odometer reading.
* Test Profile & Specs Lookup: Run option 2 to view the list of registered vehicles. Enter the ID of a vehicle to verify that the factory specifications dictionary successfully matches and displays the technical details.
* Test Fuel Logging & Validation: Run option 3 to log a fuel fill-up. Intentionally attempt to enter a new odometer reading that is lower than the current reading to verify the validation script blocks the entry.
* Test Efficiency Calculation: Log two consecutive fuel entries, then run option 4 to ensure the program correctly calculates and outputs the $\text{km/L}$ efficiency metric.
* Test Maintenance Alerts: Run option 5 to add a maintenance task (e.g., interval of 500 km, last serviced at 1000 km). Update the vehicle's odometer to 1600 km via a fuel log, then run option 6 to verify the system flags the task as overdue.
