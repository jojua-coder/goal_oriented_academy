#1 Stop gninnipS My sdroW!
def spin_words(sentence):
    sentence = sentence.split(" ")
    
    l = []
    
    for i in sentence:
        if len(i) >= 5:
            l.append(i[::-1])
        else:
            l.append(i)
    return " ".join(l)

#2 Sort the Gift Code
def sort_gift_code(code):
    return "".join(sorted(code))

#3 Search for letters
def change(st):
    alp = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    st = st.lower()
    for i in alp:
        if i in st:
            s += "1"
        else:
            s+="0"
    return s

#4 Summing a number's digits
def sum_digits(number):
    number = str(abs(number))
    sum = 0
    
    for i in number:
        sum += int(i)
    return sum