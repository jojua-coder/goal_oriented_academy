
#1 Printer Errors
def printer_error(s):
    letters = "nopqrstuvwxyz"
    result = 0
    
    for i in s:
        if i in letters:
            result += 1
            
    return f"{result}/{len(s)}"

#2 Number of People in the Bus
def number(bus_stops):
    res=0
    for i in bus_stops:
        res+=i[0]-i[1]
    return res


# 3 Don't give me five!
def dont_give_me_five(start,end):
    # your code here
      # amount of numbers
        counter = 0
        for i in range(start,end+1):
            if "5" not in str(i):
                counter+=1
        return counter

# 4 Array.diff
def array_diff(a, b):
    l = []
    for i in a:
        if i not in b:
            l.append(i)
    return l

#5 Take a Ten Minutes Walk
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count('n') != walk.count('s'):
        return False
    if walk.count('w') != walk.count('e'):
        return False
    return True