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

#2 Bit Counting
def count_bits(n):
    x = bin(n)[2:]
    result = x.count("1")
    return result