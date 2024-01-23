class Solution:
    def fruitsInTheBasket(self, fruits): # Toys in the basket
        count_map = {}
        i = 0
        max_fruits = 0
        for j in range (len(fruits)):
            count_map[fruits[j]] = 1+count_map.get(fruits[j],0)

            while len(count_map) > 2:
                count_map[fruits[i]] -= 1
                if count_map[fruits[i]] == 0:
                    del count_map[fruits[i]] 
                i += 1
            max_fruits = max(max_fruits, j-i+1)
        return max_fruits

str = 'pwwkdeew' # case 2: 'bbbb', case 3: 'a'
cls_obj = Solution()
result = cls_obj.fruitsInTheBasket(str)
print("max fruits in the basket: ", result)
