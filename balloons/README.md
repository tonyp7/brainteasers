# balloons

Write a function solution(S) that counts the number of times the word BALLOON can be written out of the string s.

For example:

```python
# Here BALLOON can be written only one time
solution('BAXXLLOON') #1

# Not enough L and O in this case to write BALLOON, so the result is 0
solution('QAWABAWONL') #0

# You can try doing this one manually, it's 3 ;-)
solution('ONLABLABLOONONLABLABLOON') #3
```

# solution

<details>
    <summary markdown="span">click to reveal</summary>
    
The key to the algorithm is to realize that you need one of each 'B', 'A', 'N', and two of each 'L' and 'O'

The first step is to count each letter appearing in a dictionary.

The 2nd step is to get the minimum of occurences of 'B', 'A', 'N' and the same for 'L' and 'O'.
We do this because if for instance you do not have at least 2 'L' and 2 'O', then you can never write BALLOON. 
In this algorithm we are simply trying to find the limiting factor.

There are three cases:
- so if minLO < 2 or minBAL < 1, we can never write BALLOON.
- if minBAL*2 <= minLO, the limiting factor is BAL, so we can only write BALLOON minBAL times
- otherwise, the limiting facotr is LO, so we can only only write BALLOON minLO times. If the number is not even it is rounded down.

Another more traditionnal approach would be to brute force the string. Each time you encounter a B for instance you create a new Balloon entry with only B. At the end of the iteration you can count how many complete balloon you have. This is suboptimal in terms of memory as the first algorithm is O(1) in space and this second approach is O(N) 

</details>
