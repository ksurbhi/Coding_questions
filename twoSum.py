class TwoSum:
  def __init__(self,arr,target):
    self.arr = arr
    self.target = target
    
  def two_Sum(self):
    my_map = {}
    for i in range(len(arr)):
      diff = target - arr[i]
      if diff in my_map:
        return [my_map[diff],i]
      my_map[arr[i]] = i


arr =[1,2,6,8,14]
target = 10
cls_obj = TwoSum(arr, target)
res = cls_obj.two_Sum()
print("sum of two elements equal to target is:", res)
