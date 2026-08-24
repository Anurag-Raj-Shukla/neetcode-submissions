class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = "".join(sorted(s))
        word2 = "".join(sorted(t))
        if(len(word1)!=len(word2)):
            return False
        else:
            if word1 == word2:
                return True
            else:
                return False