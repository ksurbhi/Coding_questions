class Solution:
 def validParenthesis(self, str):
        stack = deque()
        for i in range(len(str)):
            if str[i] == '(':
                stack.appendleft(')')
            elif str[i] == '{':
                stack.appendleft('}')
            elif str[i] == '[':
                stack.appendleft(']')
            else:
                if len(stack) ==0 or str[i] != stack[0] : # for cases like  '])' and '[)]'
                    return False
                elif str[i] == stack[0]: 
                    stack.popleft()
        if len(stack) == 0:
            return True
        else:
            return False
        
    def validParenthesis_withMap(self, str):
        stack = deque()
        mapping = {"(": ")", "{": "}", "[": "]"}
        for char in str:
            if char in mapping:
                stack.appendleft(mapping[char])           
            else:
                if len(stack) ==0 or char != stack[0]: # for cases like  '])' and '[)]'
                    return False
                elif char == stack[0]:
                    stack.popleft()               
        if len(stack) == 0:
            return True
        else:
            return False

arr = '[{()}]('
cls_obj = Solution()
# result = cls_obj.validParenthesis(arr)
result = cls_obj.validParenthesis_withMap(arr)
print(result)
