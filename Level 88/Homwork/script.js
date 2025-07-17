//1 შექმენით სარეგისტრაციო ფორმა 3 ინფუთით ემაილი, პაროლი და submit ინფუთები submit ინფუთზე დაადეთ მოვლენის მსმენელი რომელიც კლიკის დროს კონსოლში გამოიტანს ემაილს და პაროლს
let pass=document.getElementById("pass")
pass.addEventListener("click",function(e){
    e.preventDefault()

const text=pass.text.value
const password=pass.text.password

console.log(text)
console.log(password)
})

//2 
