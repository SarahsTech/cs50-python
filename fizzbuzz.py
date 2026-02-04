def main ():
    # ask the user to type a number - returns an int
    x = int(input("Enter a number: "))

    # x is divisible by 3 and 5
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")

    # else if the number is divisble by 3 
    elif x % 3 == 0:
        print("Fizz")

    #else if the number is divisible by 5
    elif x % 5 == 0:
        print("Buzz")

    # if none of the above conditions are true, this is the fallback
    else:
        print("X")

main()    