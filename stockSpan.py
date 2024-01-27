class Solution:
    def stock_Span(self, arr):
        stack = deque()
        res = []
        n = len(arr)
        # import pdb; pdb.set_trace()
        for index,value in enumerate(arr):
            while len(stack) != 0 and value >= stack[0][1]:
                stack.popleft()
            if len(stack) == 0:
                res.append(1)
            elif len(stack) != 0 and value< stack[0][1] :
                res.append( index-stack[0][0])
            stack.appendleft([index,value])
        return res
