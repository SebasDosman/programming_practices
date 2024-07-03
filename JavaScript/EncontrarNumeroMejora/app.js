const innerTextOnElement = (element, text) => {
    let tag = document.querySelector(element);
    tag.innerHTML = text;
}

const userAttempt = () => {
    alert('You have 3 attempts to guess the number');
}

innerTextOnElement('h1', '"Find Number" Game');
innerTextOnElement('p', 'Guess the number between 1 and 10');