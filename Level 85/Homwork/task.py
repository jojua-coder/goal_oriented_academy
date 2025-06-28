#1 Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#2 Count Odd Numbers below n
def odd_count(n):
    return n//2

#3 Vowel Count
def get_count(sentence):
    vowels="aeiou"
    result=0
    for i in sentence:
        if i in vowels:
             result+=1
    return result

#4 Highest and Lowest
def high_and_low(numbers):
    # ...
    num=numbers.split(" ")
    new_nams=[]
    for i in num:
        new_nams.append(int(i))
    highest=max(new_nams)
    lowest=min(new_nams)
    
    result=str(highest)+" "+str(lowest)

    return result

#5 Remove First and Last Character
def remove_char(s):
    return s[1:-1]

#6 You're a square!
def is_square(n):    
    if n < 0:
        return False
    return n ** 0.5 % 1 == 0

#7 Grasshopper - Summation
def summation(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum


