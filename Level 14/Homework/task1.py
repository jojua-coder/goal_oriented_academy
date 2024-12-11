# შეამოწმეთ არის თუ არა რიცხვი ლუწი და 10-ზე მეტი

def is_even_and_greater_than_10():
    try:
        number = int(input("შეიყვანეთ რიცხვი: "))
        if number % 2 == 0 and number > 10:
            print(f"რიცხვი {number} არის ლუწი და მეტია 10-ზე.")
        else:
            print(f"რიცხვი {number} ან კენტია, ან ნაკლებია 10-ზე.")
    except ValueError:
        print("გთხოვთ, შეიყვანოთ სწორი მთელი რიცხვი.")

# Call the function
is_even_and_greater_than_10()


# შეამოწმეთ, არის თუ არა რიცხვი 5-ზე ნაკლები ან 15-ზე მეტი

number = int(input("შეიყვანე რიცხვი: "))
if number <5:
    print(f"{number} ნაკლებია ხუთზე")

elif number > 15:
    print(f"{number} რიცხვი მეტია თხუთმეტზე")

elif 15 > number > 5:
    print(f"{number} რიცხვი მეტია ხუთზე და ნაკლებია თხუთმეტზე")
    



# შეამოწმეთ, იყოოფა თუ არა რიცხვი 3-ზე, მაგრამ არა 5-ზე


number = int(input("შეიყვანეთ რიცხვი:"))
if number % 3 == 0 and number %5 != 0:
    print(f"{number} იყოფა 3-ზე მაგრამ არ იყოფა 5-ზე")
elif number % 3 != 0 and number %5 == 0:
    print(f"{number}  არ იყოფა 3-ზე მაგრამ  იყოფა 5-ზე")
elif number % 3 != 0  and number % 5 != 0:
    print(f"რიცხვი არ იყოფა ხუთზე და არ იყოფა სამზე")


# შეამოწმეთ არის თუ არა რიცხვი 10-სა და 20-ს შორის

number =int(input("შეიყვანე რიცხვი:"))
if number >= 10 and number <=20:
    print("რიცხვი არის 10-სა და 20-ცს შორის") 

else:
    print("რიცხვი არარის 10-სა და 20-ცს შორის")


# შეამოწმეთ რიცხვი 20-ზე მეტია თუ იყოფა 4-ზე 

number =int(input("შეიყვანე რიცხვი:"))
if number > 20 and number % 4 == 0 :
    print("რიცხვი მეტია ოცზე და იყოფა 4 ზე")

elif  number < 20 and number % 4 == 0 :
    print("რიცხვი ნაკლებია ოცზე და იყოფა 4 ზე")

elif number > 20 and number % 4 != 0 :
        print("რიცხვი მეტია ოცზე და  არ იყოფა 4 ზე")

elif number < 20 and number % 4 != 0 :
        print("რიცხვი არ არის მეტია ოცზე და  არ იყოფა 4 ზე")


# შეამოწმეთ არის თუ არა რიცხვი 5-დან 10-მდე

number=int(input("შეიყვანეთ რიცხვი:"))
if number >= 5 and number <=10:
    print("რიცხვი არის 5სა და 10ს შორის")

else:
    print("რიცხვი არ არის 10-სა და 5-ს შორის")


#  შეამოწმეთ არის თუ არა რიცხვი 0-ზე მეტი და 100-ზე ნაკლები
number=int(input("შეიყვანეთ რიცხვი:"))
if number > 0 and number <=100:
    print("რიცხვი არის 0სა და 100ს შორის")

else:
    print("რიცხვი არ არის 0-სა და 100-ს შორის")