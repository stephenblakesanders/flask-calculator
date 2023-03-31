$(document).ready(function () {
    // main list for calculations
    var ops = ["0"];

    // list of operators 
    var opList = ["X", "/", "+", "-"];

    // url for posting to flask
    const url = '/data';

    // display element
    let display = document.getElementById('display');
    display.innerText = "0";

    // button elements
    let buttons = document.getElementsByClassName('button');

    // add event listener to every button
    // includes basic calculator logic 
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', (e) => {

            // true if the last value in the array is an operator
            lastOp = opList.includes(ops[ops.length - 1]);

            // true if the last value in arrray is a 0
            last0 = ops[ops.length - 1] == 0;

            // true if the only value in the array is a 0
            only0 = last0 && ops.length == 1;

            // the clicked button
            current = e.target.innerText;

            switch(e.target.innerText) {
                case 'C':
                    display.innerText = '0';
                    ops = ["0"];
                    break;

                case 'CE':
                    if (!only0) {
                        ops.pop();
                        display.innerText = display.innerText.slice(0, -1);
                    }
                    break;

                case '=':
                    const data = JSON.stringify({
                        arr: ops,
                    })
        
                    $.ajax({
                        type: "POST",
                        url: url,
                        contentType: "application/json",
                        dataType: "json",
                        data: data,
                        success: function(response) {
                            ops = [response];
                            display.innerText = response;
                        },
                        error: function(response) {
                            alert(response);
                        }
                    })

                    break;

                case '+':
                    if (!lastOp && ops.length > 0 && !last0) {
                        ops.push(current);
                        display.innerText += current;
                    }
                    break;
                
                case '-':
                    if (!lastOp && ops.length > 0 && !last0) {
                        ops.push(current);
                        display.innerText += current;
                    }
                    break;

                case '/':
                    if (!lastOp && ops.length > 0 && !last0) {
                        ops.push(current);
                        display.innerText += current;
                    }
                    break;

                case 'X':
                    if (!lastOp && ops.length > 0 && !last0) {
                        ops.push(current);
                        display.innerText += current;
                    }
                    break;

                case '0':
                    if (!only0 && !lastOp) {
                        ops.push(current);
                        display.innerText += current;
                    }
                    break;
                    
                default:
                    if (only0) {
                        ops.pop();
                        display.innerText = "";
                    }
                    display.innerText += current;
                    ops.push(current);
                    break;
           }
        })
    }
});
