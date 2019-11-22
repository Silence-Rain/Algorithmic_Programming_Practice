from queue import PriorityQueue
from typing import List

# 347. Top K Frequent Elements
def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq, res = {}, []
    for i in nums:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
            
    q = PriorityQueue()
    for key, v in freq.items():
        q.put((v * -1, key))
    for i in range(k):
        res.append(q.get()[1])
    
    return res