#1Exclamation marks series #11: Replace all vowel to exclamation mark in the
def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    
    for i in st:
        if i in vowels:
            st = st.replace(i,"!")
    return st 

#2 Surface Area and Volume of a Box
def get_size(w,h,d):
    return  [2 * (d * w + d * h + w * h),w*h*d]


#3  Find min and max
def get_min_max(seq): 
    return min(seq),max(seq)

#4 Do you speak "English"?
def sp_eng(sentence): 
    return "english" in sentence.lower()

#5 Who ate the cookie
def cookie(x):
    
    if type(x) == str: 
        return "Who ate the last cookie? It was Zach!"
    elif type(x) == int or type(x) == float:
        return  "Who ate the last cookie? It was Monica!"
    else:
        return  "Who ate the last cookie? It was the dog!"


