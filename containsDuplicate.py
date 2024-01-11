class DuplicateInArray:
    def __init__(self, arr):
        self.arr = arr

    def contains_Duplicate(self):
        my_map = {}
        for i in range(len(arr)):
            if arr[i] in my_map:
                return True
            my_map[arr[i]]  = i
        return False
arr = [1,2,3]


cls_obj = DuplicateInArray(arr)
res = cls_obj.contains_Duplicate()
print("Array has duplicate: ",res)

