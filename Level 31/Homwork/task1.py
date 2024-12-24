
#1 Function 1 - hello world
def greet():
    return "hello world!"
greet()
#2 Opposite number
def opposite(number):
    return -number
#3 Return Negative
def make_negative( number ):
    if number <0:
        return number
    else:
        return -number

#4 Sum of positive

def positive_sum(arr):
    # Your code here
    num=0
    for i in arr:
        if i>0:
            num=num+i
    return num

#5 String repeat
def repeat_str(repeat, string):
    return repeat*string

#6  Square(n) Sum
def square_sum(numbers):
    sum=0
    for i in numbers:
        sum=sum+i**2
    return sum

#7 Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)
#8 Grasshopper - Summation

def summation(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
#9 Remove String Spaces
def no_space(x):
    #your code here
    x=  x.replace(" ","")
    return x

#10 Counting sheep...
def count_sheeps(sheep):
  # TODO May the force be with you
 return sheep.count(True)