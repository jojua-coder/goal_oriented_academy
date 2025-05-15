# 1Create Phone Number
def create_phone_number(n):
    #your code here
    return   f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

#2 Find the odd int
def find_it(seq):
    result=[]
    for i in seq:
        count=seq.count(i)
        if count %2==1:
            result.append(i)
    return result[0]


#3 Array.diff
def array_diff(a, b):
    l = []
    for i in a:
        if i not in b:
            l.append(i)
    return l

#4 Is it a palindrome?
def is_palindrome(s):
    
    return s.lower() == s.lower()[::-1]




