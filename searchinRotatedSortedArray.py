class RotatedSortedArray:

    def __init__(self,arr,target):
        self.arr = arr
        self.target = target

    def search(self):
        start = 0
        end = len(self.arr)-1
        while start <= end:
            mid = int(start +(end -start)/2)
            print(mid)
            if self.arr[mid] == self.target:
                return mid
            # Search in left sorted array
            elif self.arr[start] <= self.arr[mid] :
                if self.arr[start] <= self.target <= self.arr[mid]:
                    end = mid-1
                else:
                    start = mid+1
            # search in right sorted array
            elif self.arr[mid] <= self.arr[end]:
                if self.arr[mid] <= self.target <= self.arr[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1

# Driver Code
arr = [4,5,6,0,1,2,3]
target = 8 #0, 10, 4, 3
object_of_class = RotatedSortedArray(arr, target)
res = object_of_class.search()
print(res)
