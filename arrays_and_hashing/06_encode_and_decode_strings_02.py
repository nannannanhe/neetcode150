class Solution:
    def __init__(self):
        self.sep = '#'

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for word in strs:
            encoded_str += str(len(word)) + self.sep + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i , j = 0, 0
        decoded = []
        while i < len(s):
            j = i
            while i < len(s) and s[i] != self.sep:
                i += 1
            str_len = int(s[j:i])
            word = s[i+1:i+1+str_len]
            decoded.append(word)
            i = i+1+str_len
        return decoded

