class ValidPalindrom:
    def __init__(self, str):
        self.str = str
    def is_Palindrom(self):
        i = 0
        j = len(self.str)-1
        while i <= j:
            # print(str[i], str[j])
            if self.str[i] != self.str[j]:
                return False
            else:
                i +=1
                j -=1
        return True
str = "aabbaa"
class_obj = ValidPalindrom(str)
res = class_obj.is_Palindrom()
print(res)
