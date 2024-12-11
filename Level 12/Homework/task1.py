#1  მომხმარებელს შემოატანინეთ 10 სხვადასხვა მონაცემთა ტიპი და შემდგომში type-ის მეშვეობით შეამოწმეთ მათი მონაცემთა ტიპები
name="sandro"    #str
surname="jojua"  #str
age=14    #int
height=1.63  #float
favorite_sports="basketball" #str
favorite_drink="fuse tea" #str
my_famyly_members="sali,gia,mari,luka"  #str
best_car="bmw"  #str
date_of_birthdey=04.07    #float
best_basketballer="kobi"  #str

print(type(name),type(surname),type(age),type(height),type(favorite_sports),type(my_famyly_members),type(best_car),type(date_of_birthdey),type(best_basketballer))


#2 შემოიტანეთ 3 input , 3-ვე განსხავებული ტიპის მონაცემები და მოგვიანებით type ის დახმარებით გაიგეთ მათი მონაცემები.
age_input =int(input("enter youre age: "))
height_input =float(input("enter youre height: "))
name_input = str(input("enter youre name: "))
print(type(age_input),type(height_input),type(name_input))


#3 კონვერტაცია გაუკეთეთ მთელ რიცხვს 77 სტრინგად და დაბეჭდეთ შედეგი და მისი ტიპი.
int=77
print(str(int))


#4 კონვერტაცია გაუკეთეთ სტრინგს "45.67" float ტიპად და დაბეჭდეთ მისი ტიპი.
str="45.67"
print(float(str))


#5 კონვერტაცია გაუკეთეთ ინტეჯერს 45 და აქციეთ string ტიპად და დაბეჭდეთ მისი ტიპი.
int=45
print(float(int))


