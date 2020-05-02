def remove_duplicates(test):
    new_list = []
    #dont duplicate
    for i in test:
        if i not in new_list:
            new_list.append(i)
    print(new_list)


remove_duplicates([1, 1, 2, 2])