#1 Alternate capitalization
def capitalize(s):
    result = ""

    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i]
    
    return [result, result.swapcase()]


#2 To square(root) or not to square(root)
def square_or_square_root(arr):
    
    l = []
    
    for i in arr:
        if (i ** 0.5).is_integer():
            l.append(i ** 0.5)
        else:
            l.append(i ** 2)
    return l

#3 Sort Numbers
def solution(nums):
    if nums==None:
        return []
    
    return sorted(nums)

#4 Testing 1-2-3
def solution(nums):
    if nums==None:
        return []
    
    return sorted(nums)

#5 Get Nth Even Number
def nth_even(n):
    #your code here
    return n * 2 -2

