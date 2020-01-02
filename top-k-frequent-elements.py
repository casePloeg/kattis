from collections import defaultdict
import math


class Solution:
    def topKFrequent(self, nums, k):
        freq = [set() for i in range(len(nums) + 1)]
        num_to_freq = defaultdict(int)
        for n in nums:
            index = num_to_freq[n]
            if n in freq[index]:
                freq[index].remove(n)
            num_to_freq[n] += 1
            freq[num_to_freq[n]].add(n)

        top_freq = []
        i = len(nums)
        while len(top_freq) < k:
            top_freq += list(freq[i])
            i -= 1
        return top_freq[:k]


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))