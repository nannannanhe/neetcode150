class Solution:
    def isValid(self, s: str) -> bool:
        openBracketMap = {')': '(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in openBracketMap.values():
                stack.append(char)
            if char in openBracketMap.keys():
                if len(stack)== 0 or stack[-1] != openBracketMap[char]:
                    return False
                stack.pop()
        
        if len(stack) != 0:
            return False
        return True