class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i , char in enumerate(s):
            if s.index(char)==s.rindex(char):
                return i
        retun -1
                
