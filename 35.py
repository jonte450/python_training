def check(a, b):
    if a == b:
        return True
    elif a + b == 5:
        return True
    elif abs(a - b) == 5:
        return True
    else:
        return False
    



print(check(7, 2))
print(check(3, 2))
print(check(2, 2))
print(check(7, 3))
print(check(27, 53))