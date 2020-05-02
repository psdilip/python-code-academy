def median(test):
    test = sorted(test)
    print(test)
    if len(test) % 2 == 0:
        num = int(len(test)/2)
        total = (test[num-1]+test[num])/2
    else:
        num = int(len(test)/2)
        total = test[num]
    print(total)



median([1, 34, 1, 6, 8, 0])
