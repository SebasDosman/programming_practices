let torre1 = 1;
let torre2 = 2;
let torre3 = 3;
let discos = 5;

document.write("<h3>Torres String</h3>")

torresHanoi(discos, torre1, torre3, torre2);

function torresHanoi(discos, origen, destino, aux) {
    if (discos == 1) {
        document.write("Mueva el disco " + discos + " desde la torre " + origen + " hasta la torre " + destino + "<br>");
    } else {
        torresHanoi(discos - 1, origen, aux, destino);
        document.write("Mueva el disco " + discos + " desde la torre " + origen + " hasta la torre " + destino + "<br>");
        torresHanoi(discos - 1, aux, destino, origen);
    }
};

document.write("<br>");

document.write("<h3>Torres Array</h3>")

let array1 = [];
let array2 = [];
let array3 = [];
let discos1 = 5; 

iniciarArray1();
torresHanoiArray(discos1, array1, array2, array3);

function torresHanoiArray(discos1, array1, array2, array3) {
    if (discos1 === 1) {
        moverArray(array1, array3);
        imprimirArray();
    } else {
        torresHanoiArray(discos1 - 1, array1, array3, array2);
        moverArray(array1, array3);
        imprimirArray();
        torresHanoiArray(discos1 - 1, array2, array1, array3);
    }
};

function moverArray(array1, array3) {
    array3.push(array1.pop());
};

function iniciarArray1() {
    for (let i = 0; i < discos1; i++)
        array1.push(discos1 - i);
};

function imprimirArray() {
    document.write("[ " + array1 + " ]" + "<br>");
    document.write("[ " + array2 + " ]" + "<br>");
    document.write("[ " + array3 + " ]" + "<br>");
    document.write("<br>");
};
