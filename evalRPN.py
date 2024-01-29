class Solution:
  def evalReversePolishNotaion(self, arr):
          stack = deque()
          for i in range(len(arr)):
              if arr[i] == '+':
                  stack.appendleft(stack.popleft() + stack.popleft())
              elif arr[i] == '*':
                  stack.appendleft(stack.popleft() * stack.popleft())
              elif arr[i] == '-':
                  a,b = stack.popleft() , stack.popleft()
                  stack.appendleft(b-a)
              elif arr[i] == '/':
                  a,b = stack.popleft() , stack.popleft()
                  stack.appendleft(int(b/a))
              else:
                  stack.appendleft(int(arr[i]))
          return stack[0]
              
# Driver Code
arr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
cls_obj = Solution()
# result = cls_obj.validParenthesis(arr)
result = cls_obj.evalReversePolishNotaion(arr)
print(result)
