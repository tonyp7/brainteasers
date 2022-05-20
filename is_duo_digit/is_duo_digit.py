def is_duo_digit(number):

    #represent the count of 0, 1, etc. etc.
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #transform the number to its string representation, without the negative sign if any
    str_n = str(abs(number))

    #count each number
    for c in str_n:
        counts[ int(c) ] += 1

    #check results
    #the result is basically checking the number of unique digits used. eg: if the count is > 0
    #that means the number has been used.
    unique = 0
    for count in counts:
        if count > 0:
            unique += 1

    if unique <= 2:
        return 'y'
    else:
        return 'n'



#tests
print(is_duo_digit(12))
print(is_duo_digit(-3333))
print(is_duo_digit(102))
print(is_duo_digit(789))
print(is_duo_digit(7887))
