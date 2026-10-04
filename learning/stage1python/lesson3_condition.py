pipeline_id=input("enter pipeline id:")
inlet_pressure=float(input("enter inlet_pressure:"))
outlet_pressure=float(input("enter outlet_pressure:"))
flow_rate=float(input("enter flow rate:"))
pressure_diff=inlet_pressure-outlet_pressure
print("\n pipeline reading report")
print(f"Pipeline ID:{pipeline_id}")
print(f"Inlet Pressure:{inlet_pressure}")
print(f"outlet Pressure:{outlet_pressure}")
print(f"Pressure Difference:{pressure_diff}")
print(f"Flow Rate :{flow_rate}")
if inlet_pressure<0 or outlet_pressure <0 or flow_rate<0:
    print("Status:Invalid sensor reading")
else:
    if pressure_diff<5:
        print("Status:Normal")
    elif pressure_diff<15:
        print("Status:Warning")
    else:
        print("Status:Critical")

  