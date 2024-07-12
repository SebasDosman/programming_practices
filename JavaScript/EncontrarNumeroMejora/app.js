let attempts = 1;
let secretNumber = 0;


const innerTextOnElement = (element, text) => {
    let tag = document.querySelector(element);
    tag.innerHTML = text;
}

const generateSecretNumber = () => {
    return Math.floor(Math.random() * 10) + 1;
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
    innerTextOnElement('p', 'Guess the number between 1 and 10');
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