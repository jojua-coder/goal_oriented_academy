# შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს პაროლი. პროგრამა კვლავ მოუწოდებს მოსთხვოს პაროლის შეყვანას, სანამ არ გამოიცნობს სწორ პაროლს.

pasword="secret"
secret=input("enter youre pasword: ")

while secret != pasword:
    print("არასწორი პაროლი შეიყავანე")
    secret=input("enter youre pasword: ")
print("სწორი პაროლი შეიყვანე")
