
#1 Counting sheep...
def count_sheeps(sheep):
  # TODO May the force be with you
 return sheep.count(True)

#2 Basic Mathematical Operations
def count_by(x, n):
    
    l = []
    
    for i in range(1,n+1):
        l.append(i * x)
    return l

#3 Beginner - Lost Without a Map
def maps(a):
    list=[]
    for i in a:
        list.append(i*2)
    return list



#4  Convert number to reversed array of digits
def digitize(n):
    nstring=str(n)
    ll=[]
    for i in nstring:
        ll.append(int(i))
    return ll[:: -1]  
 
#5 Reversed sequence
def reverse_seq(n):
    ll=[]
    for i in range(1,n+1):
        ll.append(i)
    return ll[:: -1]


#6 
