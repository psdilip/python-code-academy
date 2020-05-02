def purify(x):
    new_list = []
    for i in x:
        if i % 2 == 0:
            new_list.append(i)

    print(new_list)


purify([1,2,3])