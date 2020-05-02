def count(sequence, item):
    counter = 0
    for i in sequence:
        if item == i:
            counter += 1
    print(counter)

count([1, 2, 1, 1], 1)