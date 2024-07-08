


test_cases = [(3, [1, 5, 8, 3]), (-1, [1, 5, 8, 3])]

for value, group in test_cases:
    if value in group:
            print("Value is in list");
            print(f"{value} -> {group}: {True}")
    else:
            print("Value not in list!")
            print(f"{value} -> {group}: {False}")
