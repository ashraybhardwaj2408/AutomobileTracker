# Project Statement: Personal Automotive Maintenance & Expense Tracker

## 1. Problem Statement
Vehicle owners frequently struggle to maintain an organized, centralized record of their vehicle's operational costs, fuel efficiency trends, and routine maintenance schedules. Manual record-keeping on paper or scattered notes often leads to missed service intervals (such as oil changes or chain lubrication), inaccurate fuel economy calculations, and a lack of visibility into long-term vehicle health and expenses. 

## 2. Scope of the Project
This project is a modular, object-oriented Python command-line application backed by a lightweight SQLite database. Its scope encompasses:
* Managing multiple vehicle profiles (cars, motorcycles, and scooters) with persistent storage.
* Logging fuel fill-ups and automatically computing real-time fuel economy metrics (km/L).
* Scheduling routine maintenance tasks and tracking service intervals against current odometer readings.
* Providing an integrated factory specification lookup engine for popular automotive and motorcycle brands.
* Enforcing robust input validation to maintain data integrity across all system operations.

## 3. Target Users
* **Individual Vehicle & Motorcycle Owners:** People looking for a practical, fast, and offline-capable tool to track their daily vehicle upkeep.
* **Automotive Enthusiasts:** Riders and drivers who want precise data on fuel efficiency, performance specs, and maintenance histories.
* **Students & Developers:** Individuals exploring modular software design, database integration, and clean separation of concerns in Python.

## 4. High-Level Features
* **Vehicle & Fleet Management:** Full CRUD operations allowing users to register, list, and inspect vehicle profiles featuring a specialized brand selection menu.
* **Smart Factory Specifications Lookup:** Instantly retrieves manufacturer data (engine displacement, power output, torque, fuel tank capacity, and average mileage) based on the vehicle model.
* **Fuel Logging & Efficiency Engine:** Records odometer milestones, fuel volume, and total costs, automatically evaluating distance-based fuel economy.
* **Proactive Service Scheduler:** Monitors wear-and-tear milestones and triggers automated alerts for upcoming or overdue maintenance tasks.
* **Data Persistence & Safety:** Uses SQLite for reliable local data storage paired with utility input validation scripts to prevent erroneous or negative data entry.