class Solution:
    def myAtoi(self, s: str) -> int:
        number_buffer = ""
        valid_digits = ['0','1','2','3','4','5','6','7','8','9'] #simply way to check if we have a digit instead of using built in isdigit()
        lead_found = False
        value = 0 #where we store the return value
        MAX_INT32 = 2**31 - 1 #python does not have built in constants for max values of 32 bits integers
        MIN_INT32 = -2**31 
        sign = 1 #consider positive, but can switch to -1 if '-' is found

        for c in s:
            if lead_found:
                if c in valid_digits:
                    number_buffer += c
                else:
                    break
            else:
                if c in valid_digits:
                    lead_found = True
                    number_buffer += c
                elif c == '+':
                    lead_found = True
                elif c == '-':
                    lead_found = True
                    sign = -1
                elif c == ' ':
                    pass #only whitespaces can be considered as passing
                else:
                    return 0 #invalid input, for example: "abc 123"

        #if no digits found, this input is incorrect so we return 0
        #else it gets processeed
        if number_buffer == "":
            return 0
        else:
            value = int(number_buffer)
            value *= sign

        #clamp
        if value < MIN_INT32:
            value = MIN_INT32
        elif value > MAX_INT32:
            value = MAX_INT32

        return value


solution = Solution()
print(solution.myAtoi("42")) #42
print(solution.myAtoi("   -42")) #-42
print(solution.myAtoi("4193 with words")) #4193
print(solution.myAtoi("words and 987")) #0 (only whitespaces are considered leading characters)
print(solution.myAtoi("+-12")) #0 (once + OR - has been found, it should be followed by numbers to be considered valid)