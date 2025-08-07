const form = document.getElementById("myForm");
const result = document.getElementById("result");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = form.name.value;
    const surname = form.surname.value;
    let date = form.date.value;
    date = date.split("-");

    let result1 = ''

    if(date[1] === '01'){
        result1 = 'January'
    } else if(date[1] === '02'){
        result1 = 'February'
    } else if(date[1] === '03'){
        result1 = 'March'
    } else if(date[1] === '04'){
        result1 = 'April'
    } else if(date[1] === '05'){
        result1 = 'May'
    } else if(date[1] === '06'){
        result1 = 'June'
    } else if(date[1] === '07'){
        result1 = 'July'
    } else if (date[1] === '08'){
        result1 = 'August'
    } else if(date[1] === '09'){
        result1 = 'September'
    } else if(date[1] === '10'){
        result1 = 'October'
    } else if(date[1] === '11'){
        result1 = 'November'
    } else if(date[1] === '12'){
        result1 = 'December'
    }

    result.innerHTML += `
    <p>Your Fullname is: ${name} ${surname}, Your were born in ${date[0]}y, Your birth of month is ${result1}, Your day of birth is ${date[2]}</p>
    `
})