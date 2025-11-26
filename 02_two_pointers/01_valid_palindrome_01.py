class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerics = []
        for ch in s:
            if ch.isalnum():
                alphanumerics.append(ch.lower())
        reverse = alphanumerics[::-1]
        if "".join(alphanumerics) == "".join(reverse):
            return True
        return False

