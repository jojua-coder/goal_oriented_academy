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
