#1 შექმენით ფუნქცია, რომელიც დაამატებს ორ რიცხვს და აბრუნებს მათ ჯამს.
def nambers(a,b):
    print(a+b)
nambers(15,9)

#2 Sექმენით ფუნქცია, რომელიც მიიღებს სახელს და აბრუნებს მისალმებას, რომელშიც ნათქვამია "Hello".
def name(name):
    print("hello",name)
name("sandro")

#3 შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს "ლუწ" თუ რიცხვი ლუწია და "კენტი" თუ არის
def nambers1(a):
    if a %2==0:
        print("ლუწი")
    else:
        print("კენტი")
nambers1(8)

#4 შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს ამ რიცხვის გაორმაგებას.
def nambers2(namber1):
    print(namber1 * 2)
nambers2(4)


 #5 შექმენით ფუნქცია, რომელიც იღებს სიტყვას და აბრუნებს რამდენი ასო აქვს მას.
def nam1(name):
    print(len(name))
nam1("sandro")
