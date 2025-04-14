#1 Get the mean of an array
def get_average(marks):
    return sum(marks) //len(marks)

#2 Total amount of points
def points(games):
    a = 0

    for i in games:
        x = int(i.split(':')[0])
        y = int(i.split(':')[1])
        if x > y:
            a+=3
        elif x ==y:
            a += 1
    return a

#3 Number of People in the Bus
def number(bus_stops):
    res=0
    for i in bus_stops:
        res+=i[0]-i[1]
    return res

#4 Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    num1=sorted(numbers)[:2]
    return sum(num1)
 
#5 Build a square
def generate_shape(n):
    li=[]
    for i in range(n):
        li.append(n*"+")
    return "\n".join(li)

#6 Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0

    result = 0
    for i in range(number): 
        if i % 3 == 0 or i % 5 == 0 :
            result += i
        
    return result
