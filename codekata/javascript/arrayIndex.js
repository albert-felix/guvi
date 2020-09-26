// Getting input via STDIN
const readline = require("readline");

const inp = readline.createInterface({
  input: process.stdin
});

const userInput = [];

inp.on("line", (data) => {
  userInput.push(data);
});

inp.on("close", () => {
  //start-here
  //Your code goes here … replace the below line with your code logic 

    let w = parseInt(userInput[0][0]), k = parseInt(userInput[0][2]), str = userInput[1];
    let arr = str.split(" ");
    let result = [];
    
    for(let i = 0; i < arr.length-1; i++){
        if(parseInt(arr[i]) === 0){
            result.push(i+1);
        }
        else if((i+1 < arr.length) && (parseInt(arr[i+1]) === 0) ){
            result.push(i+2);      
        }
        else{
            result.push(-1);
        }
        
    }
    console.log(result.join(" "))
  //end-here
});
