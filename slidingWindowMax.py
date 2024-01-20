class Solution:
    def slidingMaximum(self, arr, k):
        queue = deque()
        result = []
        i = 0
        for j in range(len(arr)):
            if len(queue) == 0:
                queue.append(arr[j])
            else:
                queue.append(arr[j])
                while len(queue) != 0 and queue[0] < arr[j]:
                    queue.popleft()
                if j - i + 1 == k:
                    # import pdb; pdb.set_trace()
                    result.append(queue[0])
                    i = i + 1
        return result


nums = [1, 3, -2, 4, 4,-5, 6, 9, 10,10]
solution_instance = Solution()
result = solution_instance.slidingMaximum(nums, 3)
print("Maximum of all sub-windows: ", result)
