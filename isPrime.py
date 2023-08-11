from math import sqrt


# def isPrime(n):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, int(sqrt(n))+1):
#             if n % i == 0:
#                 return False
#     return True
# print(isPrime(11))
#
# def primelist(n):
#     arr = []
#     for i in range(n+1):
#        if isPrime(i)== True:
#            arr.append(i)
#     return arr
#
# var = primelist(11)
# print(var)


def maxSubArray(arr, k):
    i = 0
    sum = 0
    arr1 = []
    for j in range(len(arr)):
        import pdb

        sum = sum + arr[j]
        if j - i + 1 == k:
            arr1.append(sum)
            # print(arr1)
            sum = sum - arr[i]
            i = i + 1
    return arr1


a = maxSubArray([1, 3, 4, 5, 2, 1, 9, 2], 3)
print("Max sum of sub array of length k of an array is: ", max(a), " and ", "Min sum of sub array of length k "
                                                                           " of an array is: ", min(a))

def firstnegativenumber(arr, k):
    i =0
    list = []
    arr1 = []
    for j in range(len(arr)):
        if arr[j] <0:
            list.append(arr[j])
        if j -i +1 == k:
            if len(list) == 0:
                arr1.append(0)
                i = i + 1
            else:
                arr1.append(list[0])
                if arr[i] == list[0]:
                    list.remove(list[0])
                i = i + 1
    return arr1

a = firstnegativenumber([12,-1,-7,8,-15,30,-16,21,55,-9,0,9,8],3)
print(a)

def longest_substring_with_k_distinct(str, k):
    # str = 'aabacbebebe'
    # k =3
    i = 0
    my_map = {}
    for j in range(len(str)):
        rightchar = str[j]
        if rightchar not in my_map:
            my_map[rightchar] = 0
        my_map[rightchar] += 1
    print(my_map)

a = longest_substring_with_k_distinct('aabacbebebe',3)
print(a)


def maxisubarrays(arr,k):
    i = 0
    max_ele = []
    max_arr = []
    for j in range(len(arr)):
        max_ele.append(arr[j])
        if j-i+1 == k:
            ele = max(max(max_ele),arr[j])
            max_arr.append(ele)
            i = i+1
    print(max_arr)
    return max_arr

a = maxisubarrays([1,3,-1,-3,5,3,6,7],3)


def firstnegative(arr, k):
    i = 0
    list = []
    result = []
    for j in range(len(arr)):
        if arr[j] < 0:
          list.append(arr[j])
        if j-i+1 == k:
            if len(list) == 0:
                result.append(0)
            else:
                result.append(list[0])
                if list[0] == arr[i]:
                    list.remove(list[0])
            i = i+1
    print(result)
    return result

a = firstnegative([1,3,-1,-3,5,3,6,7],3)


def bestsellstock(arr):
