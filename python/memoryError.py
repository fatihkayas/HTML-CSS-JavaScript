try:
    lots_of_numbers = [1] * int(1e10)
except MemoryError as e:
    print(f"MemoryError: {e}")
