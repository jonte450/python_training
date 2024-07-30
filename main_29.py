def not_in(c1,c2):
    s1= set(c1)
    s2 = set(c2)
    n = s1-s2

    for i in n:
        print(i)



color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

not_in(color_list_1,color_list_2)
