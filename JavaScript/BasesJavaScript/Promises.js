const sumar = () => {
    return new Promise((resolve, reject) => {
        if (a < 0 || b < 0) {
            reject('No se puede sumar números negativos');
        } else {
            resolve(a + b);
        }
    }); 
}

const result = sumar(-3, 5).then((result) => document.write(result)).catch((error) => document.write(error));
const result1 = sumar(3, 5).then((result) => document.write(result)).catch((error) => document.write(error));

console.log(result);

document.write(result);