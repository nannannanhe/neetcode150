class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerics = []
        for ch in s:
            if ch.isalnum():
                alphanumerics.append(ch.lower())
        front, back = 0, len(alphanumerics)-1
        while front < back :
            if alphanumerics[front] != alphanumerics[back]:
                return False
            front += 1
            back -= 1
        return True
