 
#1  Remove First and Last Character Part Two
def array(string):
    string = string.split(",")
    
    if len(string) == 1:
        return None
    elif len(string) == 2:
        return None
    
    
    
    
    return " ".join(string[1:-1])

#2 Template Strings
def temple_strings(obj, feature): 
    # your code here
    return obj +" " +"are"+" "+feature


#3  Contamination #1 -String-
def contamination(text, char):
    st=""
    if text =="":
        return ""
    for i in text:
        st+=char
    return st

#4 Email Address Obfuscator
def obfuscate(email):
    for i in email:
        if i=="@":
            email=email.replace(i," [at] ")
        elif i==".":
            email=email.replace(i," [dot] ")
    return email