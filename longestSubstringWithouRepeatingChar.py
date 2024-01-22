class Solution:
    def longestSubstringWithouRepeatingChar(self, str):
        count_map = {}
        count_len = 0
        i = 0
        for j in range(len(str)):
            if str[j] not in count_map:
                count_map[str[j]] = 0
            count_map[str[j]] += 1

            while len(count_map) < j-i+1:
                count_map[str[i]] -=1
                if count_map[str[i]] == 0:
                    del count_map[str[i]]
                i += 1
            count_len = max(count_len, j-i+1)
            # print(count_len)
        return count_len


str = 'pwwkdeew' # case 2: 'bbbb', case 3: 'a'
cls_obj = Solution()
result = cls_obj.longestSubstringWithouRepeatingChar(str)
print("longest Substring Without Repeating Char",result)
