const printArray = (array) => {
    array = sumArray(array);

    for (let i = 1; i <= array.length; i++) {
        printBorder(array, i);
        printArrayIndex(array, i);
        printBorder(array, i);
    }
}

const printArrayIndex = (array, i) => {
    const PIPE_CHAR = '|';

    console.log(`${ PIPE_CHAR } ${ array[i - 1] } ${ PIPE_CHAR }`);
}

const printBorder = (array, i) => {
    const LINE_CHAR = '-';
    const SUM_CHAR = '+';
    const EQUAL_CHAR = '=';

    printLastArrayIndex(SUM_CHAR, LINE_CHAR, EQUAL_CHAR, array, i);
}

const printLastArrayIndex = (SUM_CHAR, LINE_CHAR, EQUAL_CHAR, array, i) => {
    if (i != array.length) console.log(`${ SUM_CHAR } ${ LINE_CHAR.repeat(i) } ${ SUM_CHAR }`);
    else console.log(`${ SUM_CHAR } ${ EQUAL_CHAR.repeat(i) } ${ SUM_CHAR }`);
}

const sumArray = (array) => {
    let sum = 0;

    for (let element of array) {
        sum += element;
    }

    array.push(sum);

    return array;
}


let numbersArray = [1, 23, 453, 3267, 12354, 123456];
printArray(numbersArray);