import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n <= 1 and k == 1:
            return 0
        mid = int(math.pow(2,n)/2)
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            return 1- self.kthGrammar(n-1, k-mid)
