pipeline_1 = {
    "pipeline_id": "P-101",
    "inlet_pressure": 105.0,
    "outlet_pressure": 102.0,
    "flow_rate": 42.5
}

pipeline_2 = {
    "pipeline_id": "P-102",
    "inlet_pressure": 110.0,
    "outlet_pressure": 100.0,
    "flow_rate": 38.0
}

pipeline_3 = {
    "pipeline_id": "P-103",
    "inlet_pressure": 98.0,
    "outlet_pressure": 78.0,
    "flow_rate": 45.5
}

pipelines = [pipeline_1, pipeline_2, pipeline_3]

print("\nPipeline Status Report")

for pipeline in pipelines:
    inlet_pressure = pipeline["inlet_pressure"]
    outlet_pressure = pipeline["outlet_pressure"]

    pressure_difference = inlet_pressure - outlet_pressure
    pipeline["pressure_difference"] = pressure_difference

    if pressure_difference < 5:
        status = "Normal"
    elif pressure_difference < 15:
        status = "Warning"
    else:
        status = "Critical"

    pipeline["status"] = status

    print(f"\nPipeline ID: {pipeline['pipeline_id']}")
    print(f"Inlet pressure: {pipeline['inlet_pressure']}")
    print(f"Outlet pressure: {pipeline['outlet_pressure']}")
    print(f"Flow rate: {pipeline['flow_rate']}")
    print(f"Pressure difference: {pipeline['pressure_difference']}")
    print(f"Status: {pipeline['status']}")