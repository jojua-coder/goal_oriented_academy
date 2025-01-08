#1 You Can't Code Under Pressure #1
def double_integer(i):

     return i*2

#2 
def friend(x):
    new_list = []
    for i in x:
        if len(i) == 4:
            new_list.append(i)
    return new_list

#3 
# Beginner - Reduce but Grow
def grow(arr):
    multiply=1
    for i in arr:
        multiply*=i
    return multiply

#4 Calculate average
def find_average(numbers):
    # your code here
    if numbers==[]:
        return 0
    return sum(numbers)/ len(numbers)

#5 Grasshopper - Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
     return laLiga+ copaDelRey + championsLeague

#6 Double Char
def double_char(s):
    st=""
    for i in s:
        st+=i*2
    return st

#7 Remove anchor from URL
def remove_url_anchor(url):
    index = url.find("#")
    
    
    if index >= 0:
        return url[:index]
    else:
        return url

#8 Sum of Cubes

def sum_cubes(n):
    sum = 0
    
    for i in range(n+1):
        sum += i ** 3
    return sum


# შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია
numbers=[4,7,9,8,"sandro"]
numbers.pop(2)
numbers.insert(0,"saba")
print(numbers)

# )შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ ,პირველი რიცხვი აიყვანეთ მეორე რიცხვის ხარისხში და დააბრუნეთ
def sandro(a,b):
    return a**b
print(sandro(5,8))

# შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ უნდა შეამოწმოთ ამ სიის სიგრძე თუ ლუწია დააბრუნეთ --> List length is even, ხოლო სხვა შემთხვევაში დააბრუნეთ --> List length is odd
def sandro(sia):
    if len(sia) %2==0:
        return "List length is even"
    else:
        return "List length is odd"
print(sandro([2,4,7,]))