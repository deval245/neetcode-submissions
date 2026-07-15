class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1  # shrink window from left

            seen.add(s[right])  # add current char
            max_len = max(max_len, right - left + 1)  # update max length

        return max_len

        