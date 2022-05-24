# is_duo_digit

Write a function is_duo_digit that takes as a parameter an integer. The function should return 'y' if the number is made of no more than two unique digits.

For example:

```
is_duo_digit(12) => 'y'
is_duo_digit(-3333) => 'y'
is_duo_digit(102) => 'n'
is_duo_digit(789) => 'n'
is_duo_digit(7887) => 'y'
```


# solutions

<details>
    <summary markdown="span">click to reveal</summary>
    
# solution 1: naive but completely workable approach

The solution that I propose is first of all to transform the number to a string, so that it's easy to iterate over each number without doing math (%10).

We then initialize an array of 0, with each representing the count of numbers.

So:
```
count[0] represents the numbers of 0 in the number
count[1] represents the numbers of 1 in the number
```
etc. etc.

We then iterate over the string, counting the number of digits.

The second phase of the algorithm is to simply check how many different digits have been used. That is to say, if the count is > 0, then it means the number has been used. 

This is a naive non-optimized algorithm but it doesn't run into performance issues.

# solution 2: performance

The more "aggressive" algorithm would simply return as soon as it detects a 3rd digit. So we initialize two digits: d1 and d2. Whenever There is a 3rd digit detect that is not d1 or d2, the algorith return 'n'.

If after iterating over the entire chain the case has not presented itself, it means the number is a valid duo_digit.

Both solutions give a result in O(N)

</details>