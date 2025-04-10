#1 შექმენით manual_len ფუნქცია "ფუნქციაში არ უნდა გამოიყენოთ len()"
def manual_len(a,b):
    sum=0
    for i in range(a,b):
         sum=sum+i
    return sum
print(manual_len(3,2))
