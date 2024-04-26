try:
    a = [1, 2, 3]
    print(a[5])
except IndexError as e:
    print(f"IndexError: {e}")
