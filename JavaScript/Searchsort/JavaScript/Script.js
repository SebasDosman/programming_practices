function quicksort(array) {
    document.getElementById("array").innerHTML = ("[" + array + "]");

    stack = [];

    stack.push(0);
    stack.push(array.length - 1);

    while (stack[stack.length - 1] >= 0) {
        end = stack.pop();
        start = stack.pop();

        pivotIndex = partition(array, start, end);

        if (pivotIndex - 1 > start) {
            stack.push(start);
            stack.push(pivotIndex - 1);
        }

        if (pivotIndex + 1 < end) {
            stack.push(pivotIndex + 1);
            stack.push(end);
        }
    }

    document.getElementById("arrayOrdenado").innerHTML = ("[" + array + "]");
};

function partition(arr, start, end) {
    const pivotValue = arr[end];
    let pivotIndex = start;

    for (let i = start; i < end; i++) {
        if (arr[i] < pivotValue) {
            [arr[i], arr[pivotIndex]] = [arr[pivotIndex], arr[i]];
            pivotIndex++;
        }
    }

    [arr[pivotIndex], arr[end]] = [arr[end], arr[pivotIndex]]

    return pivotIndex;
};

array = [];

let valor = prompt("Digite el valor de la potencia 10", 1);
let potencia = Math.pow(10, valor);

for (i = 0; i < potencia; i++) {
    array[i] = parseInt(Math.random() * (potencia - i));
}

quicksort(array);

var find = false;
var left = 0;
var middle = Math.round(array.length / 2);
var right = array.length;
var nbuscar = prompt("Digite el elemento a buscar", 0);
var suma = 0;
document.getElementById("search").innerHTML = ("[" + nbuscar + "]")
var operations = 0;

function buscarElemento(array, nbuscar, find, operations, left, middle, right) {
    operations++;

    if (find) {
        if (array[right] == nbuscar) {
            document.getElementById("searchFind").innerHTML = ("Encontrado en posición: " + (right + 1));
            document.getElementById("operations").innerHTML = ("Número de operaciones: " + operations);
            find = false;
        }
    
        if (suma > (array.length / 2)) {
            document.getElementById("searchFind").innerHTML = ("El elemento no se ha encontrado en el arreglo");
            find = false;
        }
    
        if (nbuscar <= array[middle]) {
            left = left;
            right = middle;
            middle = Math.round((parseInt(right) + parseInt(left)) / 2);
            buscarElemento(array, nbuscar, find, operations, left, middle, right);
        } else if (nbuscar > array[middle]) {
            left = middle;
            middle = Math.round((parseInt(right) + parseInt(left)) / 2);
            right = right;
            buscarElemento(array, nbuscar, find, operations, left, middle, right);
        }
    }
};