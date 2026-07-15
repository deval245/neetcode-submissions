from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)  # count letters in t
        window = {}
        left, right = 0, 0
        formed = 0
        required = len(need)

        min_len = float('inf')
        min_window = ""

        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]

                # Shrink window from left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

            right += 1

        return min_window
