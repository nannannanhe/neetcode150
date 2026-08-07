class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0]*26
        for r in range(len(s1)):
            s1Count[ord(s1[r])-ord('a')] += 1
            s2Count[ord(s2[r])-ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches +=1
        
        if matches == 26:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # right window check
            char_order = ord(s2[r])-ord('a')
            s2Count[char_order] +=1
            if s1Count[char_order] == s2Count[char_order]:
                matches += 1
            elif s1Count[char_order] +1 == s2Count[char_order]:
                matches -= 1

            # left window check
            char_order = ord(s2[l]) - ord('a')
            s2Count[char_order] -=1
            if s1Count[char_order] == s2Count[char_order]:
                matches += 1
            elif s1Count[char_order] -1 == s2Count[char_order]:
                matches -= 1
            l+=1

        return matches == 26
        