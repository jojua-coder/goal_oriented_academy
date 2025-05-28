//1 "!" ოპერატორზე შეასრულეთ 5 true და 5 false ოპერაციები
// false
console.log(!(5>4))
console.log(!(35>20))
console.log(!(50>10))
console.log(!(51>40))
console.log(!(73>40))

// True
console.log(!(2>4))
console.log(!(35>40))
console.log(!(50>100))
console.log(!(71>400))
console.log(!(75>500))



//2 შექმენით ცვლადი რომელშიც შეინახავთ 0-100 მდე რენდომ რიცხვს შემდეგ კი გამოიტანეთ შეფასება თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ.
let number=10;
    if(number <=90 && number<=100){
        console.log("Grade A")
    } else if(number<=80 && number<=89){
        console.log("Grade B")
    }


//3 შექმენით ცვლადი სადაც 10'ის ფარგლებში რანდომულად შეინახავთ რაღაც რიცხვს თუ ეს რიცხვი მეტი იქნება 5'ზე მაშინ დააბრუნეთ ეს რიცხვი სხვა შემთხვევაში დააბრუნეთ მისი კვადრატი.
let num=6;
    if(num > 5){
        console.log(num)
    }
    else{
        console.log(num**2)
    }

//4 შექმენით name ცვლადი სადაც შეინახავთ თქვენთვის სასურველ სახელს. თუ სახელის სიგრძე მეტია 5'ზე გამოიტანეთ "this is my friend" სხვა შემთხვევაში დააბრუნეთ ეს სახელი.
let name="sandro";
    if(name.lenght) {
        console.log("This is my freand")
    }else{
        console.log(name)
    }