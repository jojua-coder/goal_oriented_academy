 
 #1 Find the capitals
def capitals(word):
    result=[]
    
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result


 #2 Don't give me five!
def dont_give_me_five(start,end):
    # your code here
      # amount of numbers
        counter = 0
        for i in range(start,end+1):
            if "5" not in str(i):
                counter+=1
        return counter
# Fizz Buzz
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
# Invert values
def invert(lst):
    empty = []
    for num in lst:
        empty.append(num*-1)

    return empty

# Maximum Multiple
def max_multiple(divisor, bound):
    l=[]
    for i in range(1,bound+1):
        if i % divisor ==0:
            l.append(i)
    
    return max(l)