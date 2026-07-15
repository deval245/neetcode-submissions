class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if stack and ch in mapping and stack[-1]== mapping[ch]:
                stack.pop()
            else:
                stack.append(ch) 
        if not stack:
            return True
        else:
            return False
                       