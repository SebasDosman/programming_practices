/*
Tarea: Dado una variable de tipo objeto, realizar las siguientes validaciones
    1. Determinar si el perro es adulto o no
        (los perros son adultos a los 18 meses, deben convertir los dias a meses).
    2. Imprimir todas las actividades favoritas del perro con un bucle
    3. Si mide mas de un metro y pesa mas de 10 kilogramos y menos de 15 kilogramos,
        indicar que es saludable.
*/

let perro = {
    raza: "Dalmata",
    nombre: "Tommy",
    edadDias: 985,
    actividadesFavoritas: [
        "Jugar con la pelota",
        "Nadar en la piscina",
        "Morder cosas"
    ],
    peso: 12, // Kg
    altura: 110 // cm
}

let edadMeses = (perro.edadDias/30.417);
 
if (edadMeses >= 18) {
   console.log("El perro es adulto " + "\n");
} else {
    console.log("El perro no es adulto");
}

console.log("Las actividades favoritas del perro son:  ");
for (const i in perro.actividadesFavoritas) {
        console.log(perro.actividadesFavoritas[i]);
}
console.log(" ");

let alturaM = (perro.altura/100);
if (alturaM > 1 && perro.peso > 10 && perro.peso < 15) {
    console.log("El perro es saludable");
} else {
    console.log("El perro no es saludable");
}




