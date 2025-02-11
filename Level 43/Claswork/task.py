#1 Get Nth Even Number
def nth_even(n):
    #your code here
    return n * 2 -2


#2 Add Length
def add_length(str_):
    strArr = str_.split(" ")
    result = []
    
    for i in strArr:
        result.append(f"{i} {len(i)}")
    return result

#3 To square(root) or not to square(root)
def square_or_square_root(arr):
    
    l = []
    
    for i in arr:
        if (i ** 0.5).is_integer():
            l.append(i ** 0.5)
        else:
            l.append(i ** 2)
    return l


#4 Sum Mixed Array
def sum_mix(arr):
    #your code here
    sum=0
    for i in arr:
        sum += int(i)
    return sum


#5 
def find_difference(a, b):
    namravliA = 1
    namravliB = 1
    
    
    for i in a:
        namravliA *= i
    
    for i in b:
        namravliB *= i
    
    if namravliA > namravliB:
        return namravliA - namravliB
    
    elif namravliB > namravliA:
        return namravliB - namravliA
    
    return 0