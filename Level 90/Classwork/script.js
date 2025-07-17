  //1 JS'ში შექმენით ცვლადი სადაც შეინახავთ თქვენს სახელს ასევე HTML'ში შექმენით ერთი ღილაკი ღილაკზე დაადეთ მოვლენის მსმენელი და დაკლიკების დროს კონსოლში გამოიტანეთ Hello {name}!
let btn = document.getElementById("btn");

btn.addEventListener("click", function () {
    let name = "სანდრო";
    console.log(`Hello ${name}`);
});

//2  კომენტარის სახით ვრცლად ახსენით დღეს ნასწავლი სკოუპები და შეეცადეთ გააკეთოთ მაგალითებიც.
//  block scope არის რომელიც let ან const-ით გამოცხადებული ცვლადი { } ბლოკშია . local scope ცვლადი გამოცხადებულია ფუნქციის შიგნით; global scope--ცვლადი გამოცხადებულია ფუნქციის შიგნით

//3 HTML' ში შექმენით ერთი ღილაკი JS 'ში კი ერთი გლობალური ცვლადი num რომელსაც გაუტოლებთ თავიდან ნულს, შემდეგ კი JS 'ში აიდის მეშვეობით წამოიღეთ ღილაკი ამ ღილაკზე კი დაადეთ მოვლენის მსმენელი და ყოველი დაკლიკების დროს ცვლადის მნიშვნელობას დაუმატეთ 2 და გამოიტანეთ კონსოლში
let bt=document.getElementById("btn1")
let num =0;

bt.addEventListener("click", function () {
    num+=2
    console.log(num)
})

//4 შექმენით სარეგისტრაციო ფორმა თქვენთვის სასურვლეი ინფუთებით და submit ინფუთით შემდეგ JS 'ში აიდის საშუალებით წამოიღეთ ეს ინფუთი და დაადეთ მოვლენის მსენელი რომელიც დაკლიკების დროს გამოიტანს alert'ს "Registration completed successfully."
    let submitBtn = document.getElementById("fr");

    submitBtn.addEventListener("click", function () {
      alert("Registration completed successfully.");
    });