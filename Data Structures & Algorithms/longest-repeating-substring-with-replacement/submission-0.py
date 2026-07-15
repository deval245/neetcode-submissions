from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0  # count of most frequent letter in current window
        left = 0
        max_len = 0  # final answer

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])  # update max frequency in window

            # Check if more than k replacements are needed
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1  # shrink window from left
                left += 1  # move left

            # Update answer (window size)
            max_len = max(max_len, right - left + 1)

        return max_len
