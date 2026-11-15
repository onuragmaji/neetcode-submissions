from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr1 = Counter(nums)

        return [ n for n,_ in ctr1.most_common(k)]