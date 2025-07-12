#1 Correct the mistakes of the character recognition software
def correct(s):
    return s.replace("5","S").replace("0","O").replace("1","I")

#2 Grasshopper - Terminal game move function
def move(position, roll):
    return position + roll*2

#3 Return Two Highest Values in List
def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]

