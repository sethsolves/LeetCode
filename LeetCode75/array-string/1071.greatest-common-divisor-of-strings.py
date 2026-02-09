class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                candidate = str1[:i]
                
                if candidate * (n1 // i) == str1 and candidate * (n2 // i) == str2:
                    return candidate
        
        return ""
