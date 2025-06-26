//1 შექმენით ფუნქცია რომელსაც გადასცემთ მხოლოდ 1 პარამეტრს number'ს და for loop'ის მეშვეობით გამოიტანეთ ყველა რიცხვი შემოტანილი number'ის ჩათვლით
function sandro(number) {
  for (let i = 1; i <= number; i++) {
    console.log(i);
  }
}
sandro(13)
//2 შექმენით ფუნქცია რომელსაც გადასცემთ 2 პარამეტრს name და age შემდეგ შეამოწმეთ თუ შემოტანილი ასაკი ნაკლები იქნება 18 დააბრუნეთ "your not adult yet" სხვა შემთხვევაში მიესალმეთ მომხმარებელს
function my(name, age) {
  if (age < 18) {
    console.log("Your not adult yet");
  } else {
    console.log("Hello " + name);
  }
}
my("sandro", 14);

//3 შექმენით ფუნქცია რომელსაც გადაეცემა 1 პარამეტრი name შემდეგ for loop'ის საშუალებით გადაუარეთ ამ name'ის სიგრძეს და გამოიტანეთ თითოეული ასო ამ სახელიდან

function sandro1(name){
    for(let i=0;i< name.lenght; i++){
        console.log(name[i])
    }
}
sandro1("sandro")