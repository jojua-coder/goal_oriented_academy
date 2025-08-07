#1 Vowel Count
def get_count(sentence):
    vowels="aeiou"
    result=0
    for i in sentence:
        if i in vowels:
             result+=1
    return result

#2 Disemvowel Trolls
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ""
    for i in string_:
        if i not in vowels:
            result += i
    return result

#3 Highest and Lowest


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

#4 Remove First and Last Character

def remove_char(s):
    return s[1:-1]