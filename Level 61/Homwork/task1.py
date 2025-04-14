#1 List Filtering
def filter_list(l):
    filtered = []
    for i in l:
        if type(i) == int:
            filtered.append(i)
    return filtered

#2 Exes and Ohs
def xo(s):
    s=s.lower()
    return s.count("o") ==s.count("x")



 
#3 Friend or Foe?
def friend(x):
   
    new_list = []
    for i in x:
        if len(i) == 4:
            new_list.append(i)
    return new_list
