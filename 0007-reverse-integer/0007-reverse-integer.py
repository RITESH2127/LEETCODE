class Solution(object):
    def reverse(self, x):
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        if rev < -2147483648 or rev > 2147483647:
            return 0

        return rev