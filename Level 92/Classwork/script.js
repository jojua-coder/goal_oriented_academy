//2 შექმენით ერთი ღიალაკი და ერთი პარაგრაფი, ყოველ ღილაკის დაკლიკებაზე უნდა დაემატოს განსხვავებული ფერის პარაგრაფები
const colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'teal'];
    let count = 0;

    function addParagraph() {
      const p = document.createElement('p');
      p.textContent = `პარაგრაფი ${count + 1}`;
      p.style.color = colors[count % colors.length];
      document.getElementById('sandro').appendChild(p);
      count++;
    }


//5 შექმენით ცვლადი რომელშიც შეინახავთ 10 ის ფარგლებში რაიმე რენდომ რიცხვს ასევე დამატებით შექმენით კიდევ ერთი ცვლადი სადაც მომხმარებელს შემოატანინებთ რიცხვს 10 ის ფარგლებში HTML შ შექმენით ერთი ღილაკი რომელზეც მოახდენთ მოვლენის მსმენელს მასზე დაკლიკებისას თუ თქვენი რიცხვი და მომხმარებლის შემოტანილი რიცხვი ერთმანეთს დაემთხვევა გამოიტანეთ "შენ კარგად გაართვი თავი დავალებას" თუ არა მაშინ "სცადე ხელთავიდან"
const number=7;
const num=prompt("ente youre number")