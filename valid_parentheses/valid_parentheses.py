# from: https://leetcode.com/problems/valid-parentheses

class Solution:

    matches = { '(':')', '[':']', '{':'}'}

    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in self.matches:
                stack.append(c)
            else:
                # we must check if we can actually pop the stack (eg len > 0)
                # otherwise we'd run into exceptions if there were more closing
                # parentheses than openers. In any case, this mean we are facing
                # and invalid case
                if len(stack) > 0: 
                    if self.matches[stack.pop()] != c: #this is mismatch and thus no need to check further
                        return False
                else:
                    return False
            
        #if the stack is empty at the end of this it means we are good!
        #all the parentheses could be matched together.
        #note an empty string is also valid 
        return len(stack) == 0



s = Solution()
print(s.isValid('()'))
print(s.isValid('['))
print(s.isValid(']'))
print(s.isValid('{[]}'))
