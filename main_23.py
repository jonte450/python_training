def copy_two_first(str,n):
    if len(str) <= 2:
        return str * n
    else:
        two = str[:2]
        return two * n
    


print(copy_two_first('abcdef', 2))  # Output: "abab" (substring "ab" repeated 2 times)
print(copy_two_first('p', 3))  # Output: "pp" (substring "p" repeated 3 times)