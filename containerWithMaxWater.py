class WatterInTheTank:
    def __init__(self, height):
        self.height =height
    
    def container_with_most_water(self):
        low = 0
        area = 1
        high = len(self.height)-1
        print(high)
        while low < high:
            width = high - low
            area = max(min(self.height[low], self.height[high])* width, area)
            if self.height[low] <= self.height[high]:
                low +=1
            else:
                high -=1
        return area

arr = [1,8,6,2,5,4,8,3,7]
class_obj = WatterInTheTank(arr)
res = class_obj.container_with_most_water()
print(res)
