const MAX_NUMBER = 10;
let attempts = 1;
let secretNumber = 0;
let numbers = [];


const innerTextOnElement = (element, text) => {
    let tag = document.querySelector(element);
    tag.innerHTML = text;
}

const generateSecretNumber = () => {
    let number = Math.floor(Math.random() * MAX_NUMBER) + 1;
    
    if (numbers.length === MAX_NUMBER) {
        innerTextOnElement('p', 'No more attempts! Restart the game to play again.');
        return;
    } else {
        if (numbers.includes(number)) {
            return generateSecretNumber();
        } else {
            numbers.push(number);
            return number;
        }
    }
}

const clearTextOnElement = (id) => {
    document.getElementById(id).value = '';
}

const disableButton = (id, isEnable) => {
    document.getElementById(id).disabled = isEnable;
}

const restartValues = () => {
    secretNumber = generateSecretNumber();
    attempts = 1;

    innerTextOnElement('h1', '"Find Number" Game');
    innerTextOnElement('p', `Guess the number between 1 and ${ MAX_NUMBER }`);
}

const startGame = () => {
    let userNumber = parseInt(document.getElementById('userNumber').value);
    
    if (userNumber === secretNumber) {
        innerTextOnElement('p', `Congratulations! You found the number in ${ attempts } ${ attempts > 1 ? 'attempts' : 'attempt' }!`);
        disableButton('restart', false);
    } else {
        if (userNumber > secretNumber) innerTextOnElement('p', 'Try a smaller number');
        else innerTextOnElement('p', 'Try a bigger number');
        
        attempts++;

        clearTextOnElement('userNumber');
    }
}   

const restartGame = () => {
    clearTextOnElement('userNumber');
    restartValues();

    disableButton('restart', true);
}


restartValues();