class ThreeSum:
    def __init__(self, arr,target):
        self.arr = arr
        self.target = target
    def threeSum(self):
        res = []
        self.arr.sort()
        for i in range(len(self.arr)-1):
            print(i)
            low = i+1
            high = len(self.arr)-1
            while low <high:
                # print(i)
                if self.arr[i]+self.arr[low]+self.arr[high] == target:
                    res.append([arr[i],arr[low],arr[high]])
                    low += 1  # Increment low and decrement high after finding a triplet
                    high -= 1
                   
                elif self.arr[i]+self.arr[low]+self.arr[high] < target:
                    low += 1
                else:
                    high -= 1
        return res

arr = [-1,0,1,2,-1,-4]
target = 0
class_obj = ThreeSum(arr, target)
result = class_obj.threeSum()
print(result)

