from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cc = Counter(nums)
        ll = []
        for ky, val in cc.items():
            ll.append((ky, val))
        ll = sorted(ll, key = lambda x: x[1], reverse = True)

        return [l[0] for l in ll[:k]]