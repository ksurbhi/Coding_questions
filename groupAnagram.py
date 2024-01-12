class AnagramGrouper:
    def groupAnagrams(self, strs):
        result = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for l in s:
                count[ord(l)-ord('a')] += 1
            key = tuple(count)
            result[key].append(s)
        return result.values()


# Test Code
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

cls_obj = AnagramGrouper()
result = cls_obj.groupAnagrams(strs)
print(result)
