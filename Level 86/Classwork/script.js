//1 შექმენით სია და მასში გამოიტანეთ ყველა ელემენტი of keyword ით
let name=["sandro","luka","gio"]
for(let i of name){
    console.log(i)
}

//2 შექმენით სტრინგი და მასში გამოიტანეთ ყველა ასო of keyword ით
let str="sandro"
for(let i of str){
    console.log(i)
}

//3 შექმენით ობიექტი და მასში გამოიტანეთ ყველა key & value, in keyword ით
let obc={
    name:"sandro",
    userName:"jojua",
    age:"15"
}
for(let i in obc){
    console.log(`key: ${i} value: ${obc[i]}` )
}


//4 ახსენით რა არის block scope local scope global scope; block scope არის რომელიც let ან const-ით გამოცხადებული ცვლადი { } ბლოკშია . local scope ცვლადი გამოცხადებულია ფუნქციის შიგნით; global scope--ცვლადი გამოცხადებულია ფუნქციის შიგნით