# კომენტარის სახით ახსენით, თუ რა განასხვავებს tuple-ებს List-ებისგან.
#1 ის განსხვავებაა რომ tuple ბი არის შეუცვლელი ანუ მეთოდები არ მოქმედებს მაგალითად pop append remove და სხვა ხოლო ლისტებში შეგვიძლია ამ ყველაფრის გამოყენება

#2 შექმენით tuple, რომელიც შეიცავს თქვენს 5 საყვარელ ფილმს, შემდეგ კი დაბეჭდეთ პირველი და ბოლო ელემენტი ამ tuple-დან.
name=("home alone","bet men","badigtoni","spider men","ku ninzebi")
print(name[0])
print(name[4])

#3 შემენით Tuple, რომელშიც შეინახავთ კვირის დღეებს და მოახდინეთ მათი unpacking (destruction),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.
name1=("sandey","mondey","thusdey","wensdey","saterdey")
(num1,num2,num3,num4,num5)=name1
print(num1) # sandey
print(num2) #mondey
print(num3) #thusdey
print(num4) #wensdey
print(num5) # saterdey

#4  შექმენით tuple, რომელიც შეიცავს რამდენიმე ელემენტს. შემდეგ შეამოწმეთ, შეიცავს თუ არა ეს tuple კონკრეტულ ელემენტს
   # ვერ გავიგე
name=("sandro", "luka","saba")
print("saba" in name)

#5 რას გამოიტანს კოდი?
tuple = ("banana", "cherry", "strawberry", "raspberry")
(first, *second, third) = tuple
print(first) # banana
print(second) # ['cherry', 'strawberry']
print(third) # raspberry