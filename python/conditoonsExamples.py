try:
    n = int(input("Number: "))
    if n > 0:
        print("n is positive")
    elif n < 0:
        print("n is negative")
    else:
        print("n is zero")
except ValueError:
    print("Please enter a valid integer.")
