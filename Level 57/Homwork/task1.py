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