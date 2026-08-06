class Solution:
    def isValid(self, s: str) -> bool:
        openBracketMap = {')': '(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in openBracketMap:
                if not stack or stack[-1] != openBracketMap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return True if not stack else False