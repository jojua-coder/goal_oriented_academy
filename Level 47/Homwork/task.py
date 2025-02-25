# 1 Alphabetically ordered
def alphabetic(s):
    return s ==  "".join(sorted(s))

#2 Form The Minimum
def min_value(digits):
    no_duplicates = []
    
    for i in digits:
        if i not in no_duplicates:
            no_duplicates.append(i)
    
    result = ""
    
    for i in sorted(no_duplicates):
        result += str(i)
    return int(result)




#3 Fix string case
def solve(s):
    
    upper_count = 0
    lower_count = 0
    
    
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    
    if lower_count > upper_count:
        return s.lower()
    elif upper_count == lower_count:
        return s.lower()
    else:
        return s.upper()
