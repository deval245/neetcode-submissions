class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():  # Opening bracket
                stack.append(char)
            elif char in mapping:  # Closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False  # Mismatch or empty stack
                stack.pop()  # Correct match, remove last opening
            else:
                return False  # Invalid character (if given)

        return not stack  # True if stack is empty (all matched)
