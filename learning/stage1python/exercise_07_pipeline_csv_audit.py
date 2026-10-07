import csv

csv_file_path="data/sample/pipeline_readings.csv"
print("\n Pipeline CSV Audit Report")
try:
    with open(csv_file_path,mode="r",newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            pipeline_id=row["pipeline_id"]
            inlet_pressure=float(row["inlet_pressure"])
            outlet_pressure=float(row["outlet_pressure"])
            pressure_difference=inlet_pressure-outlet_pressure

            if pressure_difference<0:
                status="Invalid"
            elif pressure_difference<5:
                status="Normal"
            elif pressure_difference<15:
                status="Warning"
            else:
                 status="Critical"
            print(f"Pipeline ID:{pipeline_id}")
            print(f" Pressure Difference:{pressure_difference}")
            print(f"Status:{status}")


except FileNotFoundError:
    print(f"Error: File not found at {csv_file_path}")
except KeyError as e:
    print(f"Error: Missing column in CSV: {e}")
except ValueError as e:
    print(f"Error: Invalid number in CSV: {e}")
