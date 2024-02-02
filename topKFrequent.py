class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        heap = []
        for ele in nums:
            freq_map[ele] = 1+ freq_map.get(ele,0)
        for ele, freq in freq_map.items():
            heapq.heappush(heap,(freq,ele))
            if len(heap) > k:
                heapq.heappop(heap)
        return [ele[1] for ele in heap]
