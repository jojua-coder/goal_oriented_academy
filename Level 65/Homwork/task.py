#1 Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    num1=sorted(numbers)[:2]
    return sum(num1)

#2 List Filtering
def filter_list(l):
    filtered = []
    for i in l:
        if type(i) == int:
            filtered.append(i)
    return filtered

#3 Jaden Casing Strings
def to_jaden_case(string):
    number=[]
    st=string.split()
    for i in st:
        i=i.capitalize()
        number.append(i)
    return " " .join(number)


#4 Two to One
def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))
