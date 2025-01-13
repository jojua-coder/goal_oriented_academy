#1 Regex count lowercase letters
def lowercase_count(strng):
    counter=0
    for i in strng:
        if i.islower():
            counter +=1
    return counter

#2 Find the capitals
def capitals(word):
    result=[]
    
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result