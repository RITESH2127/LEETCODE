class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        result = ""

        # Thousands
        result += "M" * (num // 1000)
        num %= 1000

        # Hundreds
        if num >= 900:
            result += "CM"
            num -= 900
        elif num >= 500:
            result += "D"
            num -= 500
        elif num >= 400:
            result += "CD"
            num -= 400

        result += "C" * (num // 100)
        num %= 100

        # Tens
        if num >= 90:
            result += "XC"
            num -= 90
        elif num >= 50:
            result += "L"
            num -= 50
        elif num >= 40:
            result += "XL"
            num -= 40

        result += "X" * (num // 10)
        num %= 10

        # Ones
        if num == 9:
            result += "IX"
            num -= 9
        elif num >= 5:
            result += "V"
            num -= 5
        elif num == 4:
            result += "IV"
            num -= 4

        result += "I" * num

        return result