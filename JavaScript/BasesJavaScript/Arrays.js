const numeros = [1, 2, 3, 4];

// for (index in numeros) {
//     document.write("<li>" + numero + "</li>");
// }

// document.write("<ul>");

// numeros.map((numero) => document.write("<li>" + numero + "</li>"));

// document.write("</ul>");

document.write("<ul>");

const nuevo = numeros.map((numero) => numero + 1);
document.write("<li>" + nuevo + "</li>");

document.write("</ul>");