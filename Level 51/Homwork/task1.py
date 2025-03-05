#1  შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.
number=("cola","fanta","sprite","zedazeni")
(num1,num2,num3,num4,)=number
print(num1)
print(num2)
print(num3)
print(num4)

#2 შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათ
num1=("KFC","WENDYS","MC DONALDS")
num1=list(num1)
print(num1)
num1.append("BURGER")
print(num1)

#3 კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.
# აღინიშნება როგორც * ან ვარსკვლავი. ამ შემთხვევაში, იგი მოქმედებს როგორც უნივერსალური მაჩვენებელი, რაც ყველა შესაძლო ვარიანტს ან ელემენტს მოიცავს.


#4 რას გამოიტანს კოდი 
months = ("January", "February", "March", "April", "May")
(first, second, third, *fourt)= months
print(first) # January
print(second) # February
print(third) # March
print(fourt) # ['April', 'May']

