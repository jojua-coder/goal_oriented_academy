//1 for loop ის საშუალებით დაწერე რიცხვები, 2 იდან 20 ამდე, 2-2 ის გამოტოვებით
for(let i=2; i<20; i+=2){
    console.log(i)
}

//2 for loop ის გამოყენებით გადაუარეთ სტრინგის სიგრძეს, და ინდექსინგის საშუალებით გამოიტანეთ თითოეული ასო
let str = "Hello, world!";
for (let i = 0; i < str.length; i++) {
  console.log(myString[i]);
}

//3 1-დან 50 მდე გამოიტანე მხოლო ლუწი რიცხვები while loop ის გამოყენებით
let num=0;
while(num<=50){
    if(num %2===0){
        console.log(num)
    }
    num++
}

//4 while loop ის გამოყენებით დააჯამდე ლუწი რიცხვები 1 იდან 80 მდე
let nu=1;
let nu1=0;
while(nu<=80){
    if(nu1%2==0){
        nu1+=1
    }
    nu++
    console.log(nu1)
}

