rover_status = {
    "Battery":100  ,
    "Heater": "Off",
    "Camera": "Standby",
}

mission_log = {
    "Site_1":{"Site": "Crater A", "Radiation": "Low", "Water": False},
    "Site_2":{"Site": "Dune B", "Radiation": "High", "Water": True}
}

print(rover_status["Battery"])

rover_status["Battery"] = 80
rover_status["Heater"] = "On"

rover_status["Speed"] = 5

print(rover_status)

for x in mission_log:
    print (F"Site {mission_log[x]["Site"]} has {mission_log[x]["Radiation"]} radiation.")