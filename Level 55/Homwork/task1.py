# 1 შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია for loop'ის დახმარებით პირველ სიაში დაამატეთ key ხოლო მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად. 
l1=[]
l2 = []

person = {
    "name":"Giorgi",
    "last_name": "Khmaladze"
}


for i in person.keys():
    l1.append(i)

for i in person.values():
    l2.append(i)

print(l1)
print(l2)

# 2 მოცემული გაქვთ რაიმე result ცვლადი რომელშიც შეყვანილია სია [10,43,12,11,94,10,55,7,11] თქვენი დავალებაა გააქროთ ყველა დუბლიკატი ლისტიდან „თანმიმდევრობას მნიშვნელობა არაქვს“.
result=[10,43,12,11,94,10,55,7,11]
result.remove(10)
result.remove(11)
print(result)

#3 შექმენით ცარიელი dictionary შემდეგ მომხმარებელს შემოატანინეთ ჯერ key  შემდეგ კი value ამის შემდეგ თხოვეთ შეცვალოს ძველი value  და შემოატანინეთ ახალი მნიშვნელობა შემდეგ კი გამოიტანეთ საბოლოო dictionary.
key1 = input("Enter the key:")
value = input("Enter the value:")


person = {}

person[key1] = value
print(person)

new_value = input("Enter the new value: ")

person[key1] = new_value
print(person)

#4  შექმენით სეტის მსგავსი ფუნქცია რომელიც მიიღებს ლისტს და ლისტიდან წაშლის დუბლიკატებს „ფუნქციაში არ გამოიყენოთ სეტი“
l = [1,2,2,3,4,5,5,5,6,6]


def manual_set(arr):

    for i in arr:
        if arr.count(i) >=2:
            arr.remove(i)
        
        
        
    return arr
print(manual_set(l))