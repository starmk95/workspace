import { add, subtract, multiply, divide } from './math.js';

window.doAdd = function() {
    const { num1, num2 } = getValues();
    document.getElementById('result').textContent = "결과: " + add(num1, num2);
};

window.doSub = function() {
    const { num1, num2 } = getValues();
    document.getElementById('result').textContent = "결과: " + subtract(num1, num2);
};

window.doMul = function() {
    const { num1, num2 } = getValues();
    document.getElementById('result').textContent = "결과: " + multiply(num1, num2);
};

window.doDiv = function() {
    const { num1, num2 } = getValues();
    if (num2 === 0) {
        document.getElementById('result').textContent = "0으로 나눌 수 없습니다!";
    } else {
        document.getElementById('result').textContent = "결과: " + divide(num1, num2);
    }
};

function getValues() {
    return {
        num1: Number(document.getElementById('num1').value),
        num2: Number(document.getElementById('num2').value)
    };
}
