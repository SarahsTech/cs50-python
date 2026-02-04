# Write a program that asks the user to input a number and then prints whether the number is:
# Positive if it's greater than 0, negative if it's less than 0, zero if it's exactly 0.

def main():
    x = float(input("Enter a number: "))
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("zero")


main()