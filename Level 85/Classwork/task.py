#1 No zeros for heroes
def no_boring_zeros(n):
    if n==0:
        return n
    n=str(n)
    while n[-1]=="0":
        n=n[:-1]
        
    return int(n)

#2 Convert to Binary
def to_binary(n):
    return int(bin(n)[2:])
#3 Gravity Flip
def flip(d, a):
    return sorted(a) if d == "R" else  sorted(a)[::-1]

#4 Count Repeats
def count_repeats(txt):
    result = 0
    
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            result += 1
    
    return result

#5 Hamming Distance
def hamming(a,b):
    res=0
    for i in range(len(a)):
        if a[i] !=b[i]:
            res+=1
    return res

