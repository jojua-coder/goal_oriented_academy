
#1 Vowel Count
def get_count(sentence):
    vowels="aeiou"
    result=0
    for i in sentence:
        if i in vowels:
             result+=1
    return result

#2 List Filtering

def filter_list(l):
    filtered = []
    for i in l:
        if type(i) == int:
            filtered.append(i)
    return filtered

#3 Descending Order
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


#4 Isograms
def is_isogram(string):
    str = string.lower()
    return len(set(str)) == len(string)

#5 Mumbling
def accum(st):
    res=[]
    for i in range(len(st)):
        res.append(st[i].upper()+st[i].lower()*i)
    return "-".join(res) 

#6 Two to One
def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))

#7 Sum of odd numbers
def row_sum_odd_numbers(n):
    return n*n*n


