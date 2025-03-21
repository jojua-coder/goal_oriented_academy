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
    
#4 String array duplicates
def dup(arry):
    result = []
    
    for i in arry:
        test = ""

        for x in range(len(i)):
            if test == "" or i[x] != test[-1]:
                test += i[x]
                
        result.append(test)
    return result

print(dup(["abracadabra","allottee","assessee"])) 


#5 Expressions Matter
def expression_matter(a, b, c):
    l = [a*(b+c), a * b * c, (a+b) * c,a+b+c]
    
    return max(l)
  


#6 Stop gninnipS My sdroW!
def spin_words(sentence):
    sentence = sentence.split(" ")
    
    l = []
    
    for i in sentence:
        if len(i) >= 5:
            l.append(i[::-1])
        else:
            l.append(i)
    return " ".join(l)
#7 Case-sensitive!
def case_sensitive(s):
    st = []
    
    if s == "":
        return [True,[]]
    
    l = [s.islower(),st]
    
    
    if s.islower() == False:
        for i in s:
            if i.isupper():
                st.append(i)
    return l

