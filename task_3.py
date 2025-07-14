class Solution:
    def romanToInt(self, s: str) -> int:
        num_lst = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        arab = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for sym in s:
            arab += num_lst.get(sym)
        return arab


sol = Solution()
sol.romanToInt("III")
