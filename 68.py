def sum_of_dig(num):
    dig = str(num)
    total_sum = 0
    for d in dig:
        total_sum += int(d)

    return total_sum

print(sum_of_dig(5245))