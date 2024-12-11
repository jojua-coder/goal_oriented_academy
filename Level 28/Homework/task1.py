#1 დახაზე სახლლი def და for ის დახმარებით
from turtle import*
speed(10)
def squere():
        for i in range(4):
             forward(200)
             left(90)



squere()
penup()
goto(0,200)
pendown()
left(60)
def roof():
    for i in range(2):
     forward(200)
     right(120)
roof()

penup()
goto(200,0)
pendown()
forward(65)
right(90)

def door():
    for i in range(1):
        forward(70)
        left(90)
        forward(45)
        left(90)
        forward(70)
        
door()
exitonclick()










#2 შექმენი ფუქნცია სახელად add_numbers(x,b) და შემდგომში ეს ორი არგუმეტნი დაუმატე ერთმანეთს
def რიცხვი(X,z):
    print(X+z)
რიცხვი(12,32)

#3 შექმენი ფუნქცია სახელად Hello(name) და შემდგომ ფუნქციის საშუალებით დაპრინტე შენი სახელი
def hello(name):
    print(name)
hello("sandro")

#4 შექმენი ფუქნცია სახელად Multiply_Number(x,b) და შემდგომში ეს ორი არგუმეტნი გაამრავლე ერთმანეთზე
def რიცხვი1(X,z):
    print(X*z)
რიცხვი1(8,9)