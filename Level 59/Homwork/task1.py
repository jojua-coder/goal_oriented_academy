
# 1Leap Years
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
 
#2 Fizz Buzz
def fizzbuzz(n):
   
    li = []
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            li.append("FizzBuzz")
        elif i % 3 == 0:
            li.append("Fizz")
        elif i % 5 == 0:
            li.append("Buzz")
        else:
            li.append(i)
    return li


#3 