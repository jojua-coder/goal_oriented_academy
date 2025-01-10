#1 Jaden Casing Strings
def to_jaden_case(string):
    number=[]
    st=string.split()
    for i in st:
        i=i.capitalize()
        number.append(i)
    return " " .join(number)

#2 Sum of a sequence
def sequence_sum(begin, end, step):
    #your code here
    sum=0
    for i in range(begin, end+1, step ):
        sum+=i
    return sum 

#3 Regex count lowercase letters
def lowercase_count(strng):
    counter=0
    for i in strng:
        if i.islower():
            counter +=1
    return counter

#4 How good are you really
def better_than_average(class_points, your_points):
    # Your code here
        if sum(class_points) // len(class_points)  < your_points:
            return True
        else:
            return False
        
#5 Sentence Smash
def smash(words):
    return" " .join(words)


