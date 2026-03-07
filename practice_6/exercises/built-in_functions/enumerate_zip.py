names = ("Alice", "Bob", "John")
surnames = ("Smith", "Doe", "Wick")

data = enumerate(zip(names, surnames), start=1)
for index, (name, surname) in data:
    print(f"{index}. {name} {surname}")