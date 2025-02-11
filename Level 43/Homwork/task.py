#1 Jaden Casing Strings
def to_jaden_case(string):
    number=[]
    st=string.split()
    for i in st:
        i=i.capitalize()
        number.append(i)
    return " " .join(number)


#2 Reversed Words
def reverse_words(s):
    sArr = s.split()
    return " ".join(sArr[::-1])

#3 Sum of a sequence
def sequence_sum(begin, end, step):
    #your code here
    sum=0
    for i in range(begin, end+1, step ):
        sum+=i
    return sum

#4 Sum Mixed Array
def sum_mix(arr):
    #your code here
    sum=0
    for i in arr:
        sum += int(i)
    return sum

#5 Sum The Strings
def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "":
        return b
    elif b == "":
        return a
    else:
        return str(int(a) + int(b))