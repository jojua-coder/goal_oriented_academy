#1  Take the Derivative
def derive(coefficient, exponent): 
    return str(coefficient * exponent) +"x"+"^"+str(exponent -1 )


#2 Return the day

def whatday(num):
    dic ={
        1:"Sun",
        2:"Mon",
        3:"Tues",
        4:"Wednes",
        5:"Thurs",
        6:"Fri",
        7:"Satur"
    }
    
    if num > 7 or num < 1:
        return 'Wrong, please enter a number between 1 and 7'
    return dic[num] + "day"

#3 Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res.append(i)
        i = i + 1
    return res


#4 Leap Years
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
#5 For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
def quote(fighter):
    fighter = fighter.split(" ")
    l = []
    
    
    for i in fighter:
        l.append(i.capitalize())
       
    fighter = " ".join(l)
    
    

    if fighter == "George Saint Pierre":
        return "I am not impressed by your performance."
    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"