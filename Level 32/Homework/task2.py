#  შექმენით სია და ჩასვით რიცხვები 1-დან 5-მდე დასაწყისში insert()-ით ციკლის გამოყენებით.(რთული დავალებაა გაკვეთილზე განვიხილავთ)
my_list = []
for i in range(1,6):
    my_list.insert(i -1, i )
    print("Result:", my_list )