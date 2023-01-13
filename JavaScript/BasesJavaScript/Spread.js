const frutas = ["Banana", "Maçã", "Pera", "Uva", "Melancia"];
const salgados = ["Coxinha", "Kibe", "Empada", "Quibe"];

// const nuevo = frutas + salgados;
const nuevo = [...frutas, ...salgados];

document.write(frutas);
document.write(salgados);
document.write(nuevo);