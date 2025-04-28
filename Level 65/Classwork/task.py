# 1Exclamation marks series #2: Remove all exclamation marks from the end of sentence
def remove(st):
    return st.rstrip("!")

#2 Fix the loop!
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst

#3 Find the Integral
def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient // new_exponent

    return f"{new_coefficient}x^{new_exponent}"


#4 Breaking chocolate problem
def break_chocolate(n, m):
    if n==0 and m==0:
        return 0
    return n*m-1

#5 Anagram Detection
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())