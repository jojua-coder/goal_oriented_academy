#1 Credit Card Mask
def maskify(cc):
    st=""
    l= []
    for i in cc[:-4]:
        l.append(i.replace(i,"#"))
    st+=cc[-4:]
    
    return "".join(l) + st

#2  String ends with
def solution(text, ending):
    # your code here...
    return text.endswith(ending)

#3 Remove anchor from URL
def remove_url_anchor(url):
    index = url.find("#")
    
    
    if index >= 0:
        return url[:index]
    else:
        return url
    
# 4 Find the capitals
def capitals(word):
    result=[]
    
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result

#5 
def sum_cubes(n):
    sum = 0
    
    for i in range(n+1):
        sum += i ** 3
    return sum

#6 Sum of Cubes
def sum_cubes(n):
    sum = 0
    
    for i in range(n+1):
        sum += i ** 3
    return sum

#7 Sort Numbers
def solution(nums):
    if nums==None:
        return []
    
    return sorted(nums)
