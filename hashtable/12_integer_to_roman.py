# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        
        str = ""

        conversion = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I",
        }

        while num > 0:
            for key, value in conversion.items():
                while num - key >= 0:
                    str += value
                    num -= key

        str = str.replace("DCCCC", "CM").replace("CCCC", "CD")
        str = str.replace("LXXXX", "XC").replace("XXXX", "XL")
        str = str.replace("VIIII", "IX").replace("IIII", "IV")

        return str

