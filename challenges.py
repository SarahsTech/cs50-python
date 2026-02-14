while True:
    x = input("Enter a number (or q to quit): ")

    if x == "q":
        break

    x = int(x)

    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")