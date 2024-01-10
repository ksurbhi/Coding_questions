class ValidAnagram:
    def __init__(self, str, trg):
        self.str = str
        self.trg = trg

    def isAnagram(self):
        my_mapS = {}
        my_mapT ={}
        if len(str) != len(trg):
            return False
        for i in range(len(str)):
            my_mapS[str[i]] = 1 + my_mapS.get(str[i], 0)
            my_mapT[str[i]] = 1 + my_mapT.get(str[i], 0)
        return my_mapS == my_mapT


str = "mississippi"
trg = "misp"
cls_obj = ValidAnagram(str,trg)
res = cls_obj.isAnagram()
print("Array has duplicate: ",res)
