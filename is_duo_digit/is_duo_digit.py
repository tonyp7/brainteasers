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



def is_duo_digit_performance(number):
    #transform the number to its string representation, without the negative sign if any
    str_n = str(abs(number))

    d1 = ''
    d2 = ''
    for c in str_n:

        #first
        if d1 == '':
            d1 = c
        #initialize d2 to another digit found that is not d1
        elif d2 == '' and d1 != c:
            d2 = c
        #check if we have detected a 3rd digit
        elif c != d1 and c != d2: #not a duo_digit, break as soon as possible
            return 'n'

    return 'y'



#tests
print('is_duo_digit')
print(is_duo_digit(12))
print(is_duo_digit(-3333))
print(is_duo_digit(102))
print(is_duo_digit(789))
print(is_duo_digit(7887))

print('is_duo_digit_performance')
print(is_duo_digit_performance(12))
print(is_duo_digit_performance(-3333))
print(is_duo_digit_performance(102))
print(is_duo_digit_performance(789))
print(is_duo_digit_performance(7887))


