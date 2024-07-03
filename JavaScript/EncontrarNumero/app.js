const maxAttempts = 3;
const maxNumber = 10;
const secretNumber = Math.floor(Math.random() * maxNumber) + 1;
let attempts = 1;
let userNumber = 0;

while (attempts <= maxAttempts && userNumber != secretNumber) {
    userNumber = parseInt(prompt(`Insert a number between 1 and ${ maxNumber }`));
    
    if (userNumber < secretNumber) {
        alert('The number is too low');
    } else if (userNumber > secretNumber) {
        alert('The number is too high');
    } else {
        alert(`You guessed the number ${ secretNumber } with ${ attempts } ${ attempts > 1 ? 'attempts' : 'attempt'}`);
        break;
    }
    
    attempts++;
}