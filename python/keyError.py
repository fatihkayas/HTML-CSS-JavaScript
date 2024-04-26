try:
    d = {"name": "Alice"}
    print(d["age"])
except KeyError as e:
    print(f"KeyError: {e}")
