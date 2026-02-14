x = int(input("what's x? "))
y = int(input("what's y? "))

# we have two variables, each of which has values - x and y.
# we should be able to now compare these values.
# suppose I want to make a decision based on the values of these variables, I'll use the keyword "if"

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
