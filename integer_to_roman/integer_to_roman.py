# from: https://leetcode.com/problems/integer-to-roman/

class Solution:


    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    str_thousands = {'0':'', '1':'M', '2':'MM', '3':'MMM'}
    str_hundreds = {'0':'', '1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM' }
    str_tens = {'0':'', '1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC' }
    str_units = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX' }

    # Run some clever math trick to isolate each digit and simply use an array
    # that is 0 indexed to the correct digit
    def intToRoman(self, num: int) -> str:
        return self.thousands[ num // 1000] + self.hundreds[ (num % 1000) // 100 ] + self.tens[ (num % 100) // 10 ] + self.units[ num % 10]


    # This is actually faster than processing the number as an integer which is extremely counter intuitive
    # In Python transforming the number to a string and then processing the string yields about 40% perf gains
    # as compared to performing arithmetic on the number.
    def intToRomanStr(self, num:int) -> str:
        
        s = str(num)

        if num >= 1000:
            return self.str_thousands[s[0]] + self.str_hundreds[s[1]] + self.str_tens[s[2]] + self.str_units[s[3]]
        elif num >= 100:
            return self.str_hundreds[s[0]] + self.str_tens[s[1]] + self.str_units[s[2]]
        elif num >= 10:
            return self.str_tens[s[0]] + self.str_units[s[1]]
        else:
            return self.str_units[s[0]]


s = Solution()
print(s.intToRoman(2022))
print(s.intToRomanStr(2022))
print(s.intToRoman(1805))
print(s.intToRomanStr(1805))