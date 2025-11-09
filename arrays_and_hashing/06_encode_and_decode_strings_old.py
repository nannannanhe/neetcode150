class Solution:
    def __init__(self):
        self.sep = '\u0001'

    def encode(self, strs: List[str]) -> str:
        num = len(strs)
        strs.append(str(num))
        return self.sep.join(strs)

    def decode(self, s: str) -> List[str]:
        strs = s.split(self.sep)
        num = strs.pop()
        return [] if int(num) == 0 else strs

