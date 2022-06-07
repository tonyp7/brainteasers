# Integer to roman

[Original leetcode problem statement](https://leetcode.com/problems/integer-to-roman/)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

 - I can be placed before V (5) and X (10) to make 4 and 9. 
 - X can be placed before L (50) and C (100) to make 40 and 90. 
 - C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.


# Examples

## Example 1

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

## Example 2

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

## Example 3

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 

# Constraints:

1 <= num <= 3999


# Solution

<details>
    <summary markdown="span">click to reveal</summary>

First of all, despite the constraint being 1 <= num <= 3999, the problem does not say what we should do if an input is out of range,
meaning we can ignore this constraint altogether and that the input will always respect the constraint.

As for the algorithm itself, there are different ways to solve this, one by trying to be clever and substracting/adding as per the
problem statement and building a string.

The reality is this is a waste of time in this case. The more optimized algorithm is simply to realize that we can build a table 
for the entire roman numerals, as in:

|   | Thousands | Hundreds | Tens | Units |
|---|:---------:|:--------:|:----:|:-----:|
| 0 |           |          |      |       |
| 1 | M         | C        | X    | I     |
| 2 | MM        | CC       | XX   | II    |
| 3 | MMM       | CCC      | XXX  | III   |
| 4 |           | CD       | XL   | IV    |
| 5 |           | D        | L    | V     |
| 6 |           | DC       | LX   | VI    |
| 7 |           | DCC      | LXX  | VII   |
| 8 |           | DCCC     | LXXX | VIII  |
| 9 |           | CM       | XC   | IX    |

If we have these tables, the algorithm simply becomes:
 - Get string representation for thousands, add to output string
 - Get string representation for hundreds, add to output string
 - Get string representation for tens, add to output string
 - Get string representation for units, add to output string

There are two approach for this:

The first version is to consider the number as an integer and do some math to extract each digit.

This will do the trick:

```python
num = 6789
thousands = num // 1000 # = 6
hundreds = (num % 1000) // 100 # = 789 // 100 = 7
tens = (num % 100) // 10 # = 89 // 10 = 8
units = num % 10 # = 9 
```

Then we can feed these to 0 indexed array of the values:

```python
thousands_array = ['', 'M', 'MM', 'MMM']
hundreds_array = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
tens_array = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
units_array = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
```

The second version of this algorithm is to process the number as a string instead of an integer. In that case we cannot use
the index of the array to find the corresponding roman numeral. Instead we have to build a dictionnary, as in:

```python
str_thousands = {'0':'', '1':'M', '2':'MM', '3':'MMM'}
str_hundreds = {'0':'', '1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM' }
str_tens = {'0':'', '1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC' }
str_units = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX' }
```

And then we can pass each digit of the number as the key to each dictionnary.

This almost feel like cheating.

Interestingly enough, the dictionnary python version is actually faster than the array based solution, 
which is extremely counter intuitive but is actually easy to explain. Indeed writing an array in python
does not create an array, but instead create a list. This list cannot be access at O(1) speed as we would
in a typical Java or C/C++ array.

The hashmap solution in that case end up faster.

</details>

