interface Pasajero {
    nombre : String;
    hijos ?: String[];
}

const pasajero1 : Pasajero = {
    nombre : "Fernando"
}

const pasajero2 : Pasajero = {
    nombre : "Melissa",
    hijos : ["Natalia", "Miguel"]
}

function imprimeHijos(pasajero : Pasajero) : void {
    const cantHijos = pasajero.hijos?.length || 0;
    console.log(cantHijos);
}

imprimeHijos(pasajero1);