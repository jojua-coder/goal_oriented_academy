#1 Factorial
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

#2 Kebabize
def kebabize(st):
    #your code here
    s = ""
    for i in st:
        if i.isalpha():
            if i.isupper():
                s += "-" + i.lower()
            else:
                s += i
    if len(s) > 0:
        if s[0] == "-":
            s = s[1:]
    return s

#3 Isograms
def is_isogram(string):
    str = string.lower()
    return len(set(str)) == len(string)

#4 Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    x = []
    y = []
    
    for i in range(a,b+1):
        x.append(i)
    for i in range(b,a+1):
        y.append(i)
        
    if a < b:
        return sum(x)
    else:
        return sum(y)