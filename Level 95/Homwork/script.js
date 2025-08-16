const result=document.getElementById("result")

function displey(symbol){
    result.value += symbol
}

function calculate(){
   result.value = eval(result.value) 
}