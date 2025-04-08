#1 Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    pc = 0
    ns = 0
    
    for i in arr:
        if i > 0:
            pc += 1
        else:
            ns += i
            
    return [pc, ns]


#2 Are You Playing Banjo?
def are_you_playing_banjo(name):
    # Implement me!
    if name[0].lower()=="r":
        return name + " plays banjo"
    else:
        return name +  " does not play banjo"
    

#3 Simple multiplication
def simple_multiplication(number) :
    # Your code goes here
    if number %2==0:
        return number *8
    else:
        return number *9
    
#4 Invert values
def invert(lst):
    empty = []
    for num in lst:
        empty.append(num*-1)

    return empty

#5 Beginner - Reduce but Grow

def grow(arr):
    multiply=1
    for i in arr:
        multiply*=i
    return multiply
