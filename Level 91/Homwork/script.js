//1 კომენტარის სახით ახსენით როგორ იქმნება მოვლენის მსმენელი და რაში გვეხმარება იგი: მოვნელის მსმენელი იქმნება addEventlisener("click","function") გადაეცემა ორი არგუმენტი პირველი რა შეასრულოს მოვლენის დროს და მეორე თვითონ ფუნქცია  addEventlisener გამოიყენება რაღაც მოვლენის დროს

//2  კომენტარის სახით ახსენით event ბლოკი რას აკეთებს და რაში გვჭირდება ის: event ბლოკი გამოიყენება იმისთვის, რომ რეაგირება მოვახდინოთ მომხმარებლის მოქმედებაზე

//3  შექმენით საიტი თქვენთვის სასურველ თემაზე საიტზე სანამ შევალთ პირველ რიგში გააკეთეთ სარეგისტრაციო ფორმა რომელზეც მომხმარებელს შეეძლება დარეგისტრირება დაამატეთ სახელი, ემაილი, პაროლი და ასევე ერთი submit ინფუთი რეგისტრაციის დროს მომხმარებლის ინიციალები გამოვიდეს კონსოლში და გადავიდეთ მთავარ საიტზე სადაც განათავსებთ თქვენთვის სასურველ თემას 

const form = document.getElementById("forr");


form.addEventListener("submit", function(event) {
    event.preventDefault();

    
    const textValue = document.getElementById("text").value;
    const passwordValue = document.getElementById("password").value;

    
    console.log(textValue);
    console.log(passwordValue);
});
