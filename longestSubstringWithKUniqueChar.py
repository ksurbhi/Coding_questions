class Solution:
    def longestSubstringWith_k_unique(self, str, k):
        i = 0
        max_count = 0
        count_map = {}
        for j in range(len(str)):
            if str[j] not in count_map:
                count_map[str[j]] = 0
            count_map[str[j]] += 1
            while len(count_map) >k:
                count_map[str[i]] -= 1
                if count_map[str[i]] == 0:
                    del count_map[str[i]]
                i += 1
            max_count = max(max_count, j - i + 1)
        return max_count

str = 'aabacbebebe'
solution_instance = Solution()
result = solution_instance.longestSubstringWith_k_unique(str, 3)
print("lengest substring with k unique char: ", result)
