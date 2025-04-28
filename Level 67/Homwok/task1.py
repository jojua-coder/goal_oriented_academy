#1 Jaden Casing Strings
def to_jaden_case(string):
    number=[]
    st=string.split()
    for i in st:
        i=i.capitalize()
        number.append(i)
    return " " .join(number)

#2 Beginner Series #3 Sum of Numbers
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
    

#3 Maximum Length Difference
def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    
    len1= []
    len2 = []
    
    for i in a1:
        len1.append(len(i))
    
    for i in a2:
        len2.append(len(i))
     
    l = []
    for x in len1:
        for y in len2:
            l.append(abs(x - y))
    return max(l)

#4 Simple beads count
def count_red_beads(n):
    if n < 2:
        return 0
    return (n-1) * 2

#5 Simple Fun #136: Missing Values
def missing_values(seq): 
    x = 0
    y = 0
    
    
    for i in seq:
        if seq.count(i) == 1:
            x = i
        elif seq.count(i) == 2:
            y = i
    return x * x * y