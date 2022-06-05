def solution(riddle):
    possibilities = list("abc")
    output = list(riddle)
    l = len(riddle)

    for i in range(0, l):
        if output[i] == '?': 

            #get characters before and after
            char_before = ''
            char_after = ''
            if( i > 0):
                char_before = output[i-1]
            if( i < l-1):
                char_after = output[i+1]
            
            #find a suitable candidate
            p = ''
            for c in possibilities:
                if not(c == char_before or c == char_after):
                    p = c
                    break

            output[i] = p
            
    return ''.join(output)


print(solution('hello world'))
print(solution('h???? world'))
print(solution('????')) 