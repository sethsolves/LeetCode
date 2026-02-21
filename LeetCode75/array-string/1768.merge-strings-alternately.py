class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for char1, char2 in zip(word1, word2):
            merged.append(char1)
            merged.append(char2)
        remaining = word1[len(word2):] + word2[len(word1):]
        return "".join(merged) + remaining
        
