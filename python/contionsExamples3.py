try:
    # Code that might cause an exception
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
