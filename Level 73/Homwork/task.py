#1 Count characters in your string
def count(s):
    # The function code should be here
    return {i:s.count(i) for i in set(s)}

#2 The Vowel Code
def encode(st):
    return  st.translate(str.maketrans("aeiou","12345"))
    
    
def decode(st):
     return  st.translate(str.maketrans("12345","aeiou"))
 
#3 Sort Arrays (Ignoring Case)
def sortme(words):
    # your code here
    return sorted(words,key=str.lower)

# 4 Handshake problem
def get_participants(handshakes):
    n=0
    while (n*(n-1)) //2 < handshakes:
        n+=1
    return n

