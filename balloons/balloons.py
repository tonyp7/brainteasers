def solution(S):
    count = {'B':0,'A':0,'L':0,'O':0,'N':0}
    keys = count.keys()

    #count
    for char in S:
        if char in keys:
            count[char] += 1
    
    #check results: check the minimum of L and O and B A N to see which one is the limiting factor
    doubles = min(  count['L'], count['O'])
    singles = min(  count['B'], count['A'], count['N'] )

    
    if doubles < 2 or singles < 1: #this can never work
        return 0
    elif singles*2 <= doubles: #limited factor: B A N
        return singles
    else: #limiting factor: O L
        return int(doubles / 2) #here we take advantage of the fact int() will work as floor



S = 'BAXXLLOON'
print( '{S}: ', solution(S))

S = 'QAWABAWONL'
print( '{S}: ', solution(S))

S = 'ONLABLABLOON'
print( '{S}: ', solution(S))

S = 'ONLABLABLOONONLABLABLOON'
print( '{S}: ', solution(S))