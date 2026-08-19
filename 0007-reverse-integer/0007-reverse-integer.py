class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        rev = sign * int(str(abs(x))[::-1])
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        return rev