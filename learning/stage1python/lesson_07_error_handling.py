import csv

csv_file_path = "data/sample/pipeline_readings.csv"

try:
    with open(csv_file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            pipeline_id = row["pipeline_id"]
            inlet_pressure = float(row["inlet_pressure"])
            outlet_pressure = float(row["outlet_pressure"])
            flow_rate = float(row["flow_rate"])

            print(f"Read pipeline: {pipeline_id}")

except FileNotFoundError:
    print(f"Error: File not found at {csv_file_path}")
except KeyError as e:
    print(f"Error: Missing column in CSV: {e}")
except ValueError as e:
    print(f"Error: Invalid number in CSV: {e}")