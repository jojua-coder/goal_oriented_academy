#1 Reversed Strings
def solution(string):
    return string[::-1]

#2 Sum Arrays
def sum_array(a):
    return sum(a)
#3 IP Validation
def is_valid_IP(strng):
    res = strng.split(".")
    for i in res:
        if i.isdigit() == False or len(res) != 4:
            return False
        if i.startswith("0") and len(i) > 1 or int(i) > 255:
            return False
    return True