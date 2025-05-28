#1 Beginner - Reduce but Grow
def grow(arr):
    multiply=1
    for i in arr:
        multiply*=i
    return multiply


#2 Beginner Series #2 Clock
def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000

#3 A Needle in the Haystack
def find_needle(haystack):
    name=haystack.index("needle")
    return  f"found the needle at position {name}"

#4 Transportation on vacation
def rental_car_cost(d):
    # your code
    if d >=7:
        return d*40-50
    elif d >=3:
        return d*40-20
    else:
        return d*40
    

# 5 Is this a triangle?
def is_triangle(a, b, c):
    return a+c>b and b+c>a and b+a>c 
