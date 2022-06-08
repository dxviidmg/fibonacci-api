def fibonacci(index):
    n1, n2 = 0, 1
    count = 0

    if index < 0:
        return "Please enter a positive integer"
    elif index == 0:
        return n1
    elif index in [1, 2]:
        return n2
    else:
        while count < index-1:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth