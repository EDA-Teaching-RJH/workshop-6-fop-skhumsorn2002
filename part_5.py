status = {
    "Power": 100,
    "Sample": 0,
}
item_sample = []

while True:
    if status["Power"] != 0:
        print("----------Initialising----------")
        while True:
            try:
                print("a.Dig for Sample \nb.Report Status \nc.Emergency Stop")
                option = str(input("Menu access (a/b/c):"))
            except ValueError:
                print("Invalid input1")
            else:
                break

        if option == "a":
            print("----------Initialising----------")
            new_sample = input("Enter discovered sample: ")
            item_sample.append(new_sample)
            status["Sample"] = len(item_sample)
            status["Power"] = status["Power"] - 50

        elif option == "b":
            print("----------Initialising----------")
            print(status)

        elif option == "c":
            print("----------Initialising----------")
            print("Terminate mission")
            break

        else:
            print("Invalid input2")

    else:
        print("----------Initialising----------")
        print("Power depleted")
        print("Terminate mission")
        break
print(status)
print(item_sample)