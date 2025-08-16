#1 Convert PascalCase string into snake_case
def to_underscore(strng: str) -> str:
    strng = str(strng)
    result = strng[0].lower()
    for i in strng[1:]:
        if i.isupper():
            result += "_" + i.lower()
        else:
            result += i.lower()
    return result


#2 Count Repeats
def count_repeats(txt):
    result = 0
    
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            result += 1
    
    return result

#3 String transformer
def string_transformer(s):
    swapped = s.swapcase()
    return " ".join(swapped.split(" ")[::-1])