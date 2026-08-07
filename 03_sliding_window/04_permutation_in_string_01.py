class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            ws = list(s1)
            j = i
            while j < len(s2) and s2[j] in ws:
                ws.remove(s2[j])
                j +=1
            if not ws:
                return True
        return False