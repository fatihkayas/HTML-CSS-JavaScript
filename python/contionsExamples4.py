import array

try:
    a = array.array('i', range(10**9))  # Allocating a large array
except MemoryError as e:
    print(f"MemoryError: {e}")
except NameError as e:
    print(f"NameError: {e}")