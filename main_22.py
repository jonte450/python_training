def count_four(lst):
    count = 0
    for el in lst:
        if el == 4:
            count = count+ 1
    return count


print(count_four([1, 4, 6, 7, 4]))  # Output: 2 (There are two occurrences of 4 in the list.)
print(count_four([1, 4, 6, 4, 7, 4]))  # Output: 3 (There are three occurrences of 4 in the list.)


    
