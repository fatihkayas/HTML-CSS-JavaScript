try:
    # Code that might cause an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if there is a ZeroDivisionError
    print("You can't divide by zero!")
