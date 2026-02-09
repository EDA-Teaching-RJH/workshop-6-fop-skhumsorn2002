travel_log = []

while True:
    while True:
        try:
          reading = int(input("Sensor Reading (Slope Angle): "))
        except ValueError:
            print("Sensor Glitch")
        else:
            break

    if reading > 45:
        print("CRITICAL TILT! HALTING.")
        break
    else:
        travel_log.append(reading)
        print("Path Stable. Moving forward.")
        continue

print("Mission Terminated")
print(F"Total step taken: {len(travel_log)}")

for i in range(len(travel_log)):
    print(F"Log {i+1} angel: {travel_log[i]}")