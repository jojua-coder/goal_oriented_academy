#1 You Can't Code Under Pressure #1
def double_integer(i):

     return i*2


 #2 Returning Strings
def greet(name):
    #Good Luck (like you need it)
    return  f"Hello, {name} how are you doing today?"


 
#3 Sum Arrays

def sum_array(a):
    return sum(a)

#4 Remove exclamation marks
def remove_exclamation_marks(s):
     return s.replace("!","")


#5 #2 Find the capitals
def capitals(word):
    result=[]
    
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result