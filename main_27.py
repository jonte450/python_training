def concat(input_list):
    concat_s = ''
    for elem in input_list:
        concat_s += str(elem)
    return concat_s



example_list = [1, 'apple', 3.14, 'banana']
result = concat(example_list)
print(result)