class Solution:
    def topKFrequent(self, nums, k):
        count_map = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count_map[num] = 1+count_map.get(num, 0)
        print(count_map)

        for num, count in count_map.items():
            freq[count].append(num)
        print(freq)
        result = []
        for i in range (len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)
            if len(result) == k:
                return result


# O(n)

# nums = [1,1,1,2,2,2,3,3,4,4,5]
# k=2
nums = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
k = 2

solution_instance = Solution()
result = solution_instance.topKFrequent(nums, k)

print(result)
