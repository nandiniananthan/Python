class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep = ""
        n = len(s)

        for i in range(len(s) // 2):
            rep += s[i]
            if len(s) % len(rep) == 0:
                if (rep * (len(s) // len(rep))) == s:
                    return True


def repeatedSubstringPattern(s):
        ans = s in (s + s)[1: -1]
        print(ans)
        return ans
    

repeatedSubstringPattern("abab")