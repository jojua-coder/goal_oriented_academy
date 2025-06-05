#1 Make a function that does arithmetic!
def arithmetic(a, b, operator):
    if operator=="add":
        return a+b
    elif operator=="subtract":
        return a-b
    elif operator=="multiply":
        return a*b
    else:
        return a/b
    
#2 Anagram Detection
# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

#3 Count by X
def count_by(x, n):
    
    l = []
    
    for i in range(1,n+1):
        l.append(i * x)
    return l

# 4 Third Angle of a Triangle
def other_angle(a, b):
    return 180-a-b

#5 Third Angle of a Triangle
def sum_even_numbers(seq): 
    # your code here
    res=[]
    for i in seq:
        if i%2==0:
            res.append(i)
            
    return sum(res)

#6 Sum The Strings
def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "":
        return b
    elif b == "":
        return a
    else:
        return str(int(a) + int(b))
    
#7 Remove the minimum
def remove_smallest(numbers):
    if numbers == []:
        return []
    
    x = numbers.copy()
    min_number = min(x)
    index = x.index(min_number)
    x.pop(index)
    return x
 
#8 Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
#     [humanYears,catYears,dogYears]
    res = [human_years,0,0]
    if human_years == 1:
        res[1] = 15
        res[2] = 15
    elif human_years == 2:
        res[1] = 15 + 9
        res[2] = 15 + 9
    elif human_years > 2:
        res[1] = 15 + 9 + (4 * (human_years -2))
        res[2] = 15 + 9 + (5 * (human_years - 2))
    return res