//1  შექმენით ობიექტი დასაც ჩამოწერთ თქვენს თავზე ინფორმაციას, შემდეგ ამ ობიექტიდან გამოიტანეთ თქვენი სახელი და გვარი.
let sand ={
    name:"sandro",
    surname:"jojua",
    age:"14",
    BestAcademy:"Goa"
}
console.log(sand.name)
console.log(sand.surname)

//2  შექმენით ობიექტი სადაც შეიყვანთ სახელსა და გვარს შემდეგ კი გაანახლეთ მათი value'ბი და გამოიტანეთ ეს ობიექტი. 
let number={
    name1:"sandro",
    surname1:"jojua"
}
number.name1="saba"
console.log(number.name1)
number.surname1="gulordava"
console.log(number.surname1)



//3  დაწერეთ დღეს შესწავლილი var' ის შესახებ და შეადარეთ იგი let და const'ს.
// var არის ძალიან ცუდი გზა ცვლადების შესაქმნელად და (ვინდოუს ობიექტში ახდენს ცვლილებას) let ის მნიშვნელობის შეცვლა შეგვიძლია ხოლო const ის არა

//4 შექმენით ცვლადი რომელსაც გადასცემთ სტრინგს შემდეგ კი დააბრუნეთ ამ ცვლადის სიგრძე.
let sandro= "jojua"
console.log(sandro.length)


// 5 შექმენით ცვლადი და გადაიყვანეთ იგი uppercase'ში შემდეგ კი lowercase'ში. 
let surname="jojua";
console.log(surname.toUpperCase())
console.log(surname.toLocaleLowerCase())