class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize result array with 0
        stack = []  # Monotonic stack to store indices

        for i in range(n):
            # While current temp is higher than the temp at index stored in stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index  # Days waited for warmer temp

            # Add current index to stack
            stack.append(i)

        return result
