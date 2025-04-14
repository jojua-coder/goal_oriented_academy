#1 Jaden Casing Strings
def to_jaden_case(string):
    number=[]
    st=string.split()
    for i in st:
        i=i.capitalize()
        number.append(i)
    return " " .join(number)


#2 Isograms
def is_isogram(string):
    str = string.lower()
    return len(set(str)) == len(string)

#3 Sum of odd numbers
def row_sum_odd_numbers(n):
    return n*n*n


#4 Mumbling
def accum(st):
    res=[]
    for i in range(len(st)):
        res.append(st[i].upper()+st[i].lower()*i)
    return "-".join(res)

#5 Regex validate PIN code
def validate_pin(pin):
    if len(str(pin)) == 4 or len(str(pin)) == 6:
        pass
    elif not pin.isdigit:
        return False

    else:
        return False
    pin = list(str(pin))
    for i in pin:
        if not i.isdigit() or not i.isdigit:
            return False 

    return True