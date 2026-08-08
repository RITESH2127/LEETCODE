class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = ""

        for i in range(len(values)):
            count = num // values[i]

            if count > 0:
                result += symbols[i] * count
                num %= values[i]

        return result