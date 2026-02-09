while True:
    try:
        speed = int(input("Enter Motor Speed:"))
    except ValueError :
        print ("Error: Corrupted Signal. Maintaining current speed.")
    else:
        break

def main():
    while True:
        coordinate = get_coordinate()
        if coordinate < -100 or coordinate > 100:
            print("Coordinate out of range")
        else:
            print(F"Set Coordinate to {coordinate}")
            break

def get_coordinate():
    while True:
        try:
            x_coordinate = int(input("Enter an X-coordinate: "))
            return x_coordinate
        except ValueError:
            print("Invalid coordinate")

main()