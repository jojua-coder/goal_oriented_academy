# კომენტარის სახით ჩამოწერეთ თუ რა განსხვავებაა set-ებსა და list-ებს შორის.
#1 set ში ის განსხვავებაა რომ აქ ხდება დუბლიკატების წაშლა მაგალითად აქ name={2,1,3,2} 2 იანი ავტომატურად ამოვარდება რადგან დუბლიკატია და ასევევ დაპრინტვის დროს ადგილებს იცვლის რადგან მათ ინდექსი არ გააჩნიათ


#2 შექმენით set სადაც შეინახავთ რიცხვებს, შემდეგ კი ინდექსინგის საშუალებით სცადეთ თითოეული ელემენტის შეცვლა და დააკვირდით შედეგს.
name={"sandro","saba","luka","nika"}
print(name)


#3 შექმენით set, რომელშიც შენახული გექნებათ Fast food საკვები პროდუქტები. შემდეგ კი ამოშალეთ ყველა პირვანდელი ელემენტები set-იდან, და მათ ნაცვლად დაამატეთ ჯანსაღი საკვები პროდუქტები.
fast_food={"burger","shaurma","piza","sendvichi"}
fast_food.remove("burger")
fast_food.remove("shaurma")
fast_food.remove("piza")
fast_food.remove("sendvichi")
print(fast_food)
fast_food.add("salati")
fast_food.add("pile")
fast_food.add("kvercxi")
fast_food.add("kitri")
print(fast_food)


