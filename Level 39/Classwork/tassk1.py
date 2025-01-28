# 1 reverseIt
def reverse_it(data):
    if type(data) == str:
        data = data[::-1]
    elif type(data) == int:
        data = int(str(data)[::-1])
    elif type(data) == float:
        data = float(str(data) [::-1])
        
    return data


#2  Generate range of integers
def generate_range(start, stop, step):
    ell=[]
    for i in range(start,stop+1,step):
        ell.append(i)
    return ell

#3 Sum without highest and lowest number
def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) <= 2:
        return 0
    
    return sum(arr) - max(arr) - min(arr)

#4 Count by X
def count_by(x, n):
    
    l = []
    
    for i in range(1,n+1):
        l.append(i * x)
    return l  