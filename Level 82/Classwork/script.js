//1 მომხარებელს შემოატანინეთ ციფრი, შემდეი 0 იდან ამ რიცზვამდე დაპრინტეთ ყველა რიცხვი, დაიხმარეთ რესურები, გამოიყენეთ while loop (javascript) (NOT python)
let number = parseInt(prompt("enter your number"));
while (number > 0) {
    console.log(number);
    number--;
}


//2 მომხარებელს შემოატანინეთ სახელი, შემდეგ სანამ ამ სახელის სიგრძე ნაკლებია 10ზე, შემოატანინეთ ახლიდან 
// გამოიყენეთ while loop (javascript) (NOT python)
let number1 = prompt("enter your number");
while (number1.length > 10) {
    number1 = prompt("more again");
}


//3 მომხარებელს შემოატანინეთ პინკოდი, შემდეგ სანამ ეს პინკოდი არ უდრის 6446 ს, შემოატანინეთ ახლიდან
// გამოიყენეთ while loop (javascript) (NOT python)
let pin = prompt("enter your pin code");
while (pin != "6446") {
    pin = prompt("more again");
}


//4 მომხარებელს შემოატანინეთ პაროლი, სანამ ეს პაროლი არ უდრის "ვანოჩკა" ს, შემოატანინეთ ახლიდან
// გამოიყენეთ while loop (javascript) (NOT python)
let password = prompt("enter your password");
while (password != "გონჩხა") {
    password = prompt("enter your password again");
}
