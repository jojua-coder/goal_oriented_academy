#1 Count by X
def count_by(x, n):
    result=[]
    
    for i in range(x, x*n+1,x):
         result.append(i)
    
    return result

#2 Thinkful - Logic Drills: Traffic light
def update_light(current):
    dict={
        'green':'yellow',
        'yellow':'red',
        'red':'green'
    }

    return dict.get(current)

#3 Count of positives / sum of negatives
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


#4 Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

 
#5 Abbreviate a Two Word Name

def abbrev_name(name):
    name = name.upper()
    name = name.split()
    name1 = name[0][0]
    name2 = name[1][0]
    return f"{name1}.{name2}"