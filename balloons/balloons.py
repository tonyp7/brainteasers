def solution(S):
    count = {'B':0,'A':0,'L':0,'O':0,'N':0}
    keys = count.keys()

    #count
    for char in S:
        if char in keys:
            count[char] += 1
    
    #check results: L and O is the limiting factor
    doubles = min(  count['L'], count['O'])
    singles = min(  count['B'], count['A'], count['N'] )

    #this can never work
    if doubles < 2 or singles < 1:
        return 0
    elif singles*2 <= doubles:
        return singles
    else:
        return int(doubles / 2)



S = 'BAXXLLOON'
print( '{S}: ', solution(S))

S = 'QAWABAWONL'
print( '{S}: ', solution(S))

S = 'ONLABLABLOON'
print( '{S}: ', solution(S))

S = 'ONLABLABLOONONLABLABLOON'
print( '{S}: ', solution(S))