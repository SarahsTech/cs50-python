# input("what's x?"") does what's inside the innermost () first.
# always returns the result as a string, like "5"
# int() or float() takes the result from input() - which is a string.
# converts it to an integer "5" -> 5

x = float(input("What's x?"))
y = float(input("What's y?"))

z = round(x + y)

print(f"{z:.2f}")
