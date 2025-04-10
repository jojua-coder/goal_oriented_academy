#1 შექმენით manual_len ფუნქცია "ფუნქციაში არ უნდა გამოიყენოთ len()"
def manual_len(a):
    sum=0
    for i in a:
         sum+=1
    return sum
print(manual_len("123456"))
