array2 = [];
array3 = [];
array4 = [];

let valor = prompt("Digite el valor de la potencia 10", 0);
let potencia = Math.pow(10, valor);

for (i = 0; i < potencia; i++) {
    array2[i] = i + 1;
}

for (i = 0; i < potencia; i++) {
    array3[i] = potencia - i;
}

for (i = 0; i < potencia; i++) {
    array4[i] = parseInt(Math.random() * (potencia - i));
}

function burbuja(array) {
    var a = 0;

    console.time();

    for (i = 0; i < array.length; i++) {
        for (j = i + 1; j < array.length; j++) {
            if (array[i] > array[j]) {
                a = array[j];
                array[j] = array[i];
                array[i] = a;

                a++;
            }
        }
    }

    console.timeEnd();

    document.getElementById("burbuja").innerHTML = a;

    document.getElementById("array1").innerHTML = ("[" + array + "]");
    console.log(" ");
};

function burbuja2(array) {
    var a = 0;

    for (i = 0; i < array.length; i++) {
        for (j = i + 1; j < array.length; j++) {
            if (array[i] < array[j]) {
                a = array[j];
                array[j] = array[i];
                array[i] = a;

                a++;
            }
        }
    }

    console.log(a);
    document.getElementById("burbuja2").innerHTML = a;

    document.getElementById("array2").innerHTML = ("[" + array + "]");
    console.log(" ");
};

function burbuja3(array) {
    let cont = 0;

    console.time();

    for (i = 0; i < array.length; i++) {
        for (j = 0; j < array.length; j++) {
            if (array[j] > array[j + 1]) {
                a = array[j];
                array[j] = array[j + 1];
                array[j + 1] = a;

                cont++;
            }
        }
    }

    console.timeEnd();

    document.getElementById("burbuja3").innerHTML = cont;

    document.getElementById("array2.1").innerHTML = ("[" + array + "]");
    console.log(" ");
};

function insercion(array) {
    let tam = array.length, temp, a = 0, i = 0;

    console.time();

    for (let j = 1; j < tam; j++) {
        temp = array[j];
        i = j - 1;

        while (i >= 0 && array[i] > temp) {
            array[i + 1] = array[i];

            i--;

            a++;
        }

        array[i + 1] = temp;
    }

    console.timeEnd();

    document.getElementById("insercion").innerHTML = a;

    document.getElementById("array3").innerHTML = ("[" + array + "]");
    console.log(" ");
};

function seleccion(array) {
    let tam = array.length, minimo, temp, a = 0;

    console.time();

    for (let i = 0; i < tam; i++) {

        minimo = i;

        for (let j = i + 1; j < tam; j++) {
            if (array[minimo] > array[j]) {
                minimo = j;
            }

            a++;
        }
        temp = array[i];
        array[i] = array[minimo];
        array[minimo] = temp;
    }

    console.timeEnd();

    document.getElementById("seleccion").innerHTML = a;

    document.getElementById("array4").innerHTML = ("[" + array + "]");
    console.log(" ");
};

function quicksort(array) {
    let a = 0;

    stack = [];

    stack.push(0);
    stack.push(array.length - 1);

    console.time();

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

        a++;
    }

    console.timeEnd();

    document.getElementById("quicksort").innerHTML = a; 

    document.getElementById("array5").innerHTML = ("[" + array + "]");
    console.log(" ");
};

function partition(arr, start, end){
    let a = 0;
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