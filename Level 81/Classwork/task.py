#1 Super Duper Easy
def problem(a):
    #Easy Points ^_^
    if type(a)==str:
        return "Error"
    else:
        return (a*50) + 6
    
#2 They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
def is_opposite(s1,s2):
    if s1 == "" or s2 == "":
        return False
    return s1 == s2.swapcase()

#3 Chuck Norris VII - True or False? (Beginner)
def if_chuck_says_so():
    return not True