import csv

csv_file_path = "data/sample/pipeline_readings.csv"

print("Pipeline Readings from CSV")

with open(csv_file_path, mode="r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        pipeline_id = row["pipeline_id"]
        inlet_pressure = float(row["inlet_pressure"])
        outlet_pressure = float(row["outlet_pressure"])
        flow_rate = float(row["flow_rate"])

        pressure_difference = inlet_pressure - outlet_pressure

        if pressure_difference < 0:
            status = "Invalid"
        elif pressure_difference < 5:
            status = "Normal"
        elif pressure_difference < 15:
            status = "Warning"
        else:
            status = "Critical"

        print(
            f"Pipeline ID: {pipeline_id} | "
            f"Diff: {pressure_difference:.1f} | "
            f"Status: {status}"
        )