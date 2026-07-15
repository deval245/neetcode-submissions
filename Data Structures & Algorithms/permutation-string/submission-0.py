class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  # Impossible if s1 is longer than s2

        # Initialize frequency arrays
        s1_count = [0] * 26
        window_count = [0] * 26

        # Fill counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # Check if initial window matches
        if s1_count == window_count:
            return True

        # Slide window
        for i in range(len(s1), len(s2)):
            # Add new character to the window
            window_count[ord(s2[i]) - ord('a')] += 1
            # Remove character that is no longer in window
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Check if current window matches
            if s1_count == window_count:
                return True

        return False  # No match found
