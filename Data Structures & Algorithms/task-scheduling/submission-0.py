class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
         freq = list(Counter(tasks).values())
         max_freq = max(freq)
         count_max = freq.count(max_freq)

         intervals = (max_freq - 1) * (n + 1) + count_max

         return max(len(tasks), intervals)