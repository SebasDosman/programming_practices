function sumar(a : number, b : number) : number {
    return a + b;
}

const sumarFlecha = (a : number, b : number) : number => {
    return a + b;
}

function multiplicar(numero : number, base : number , otroNumero? : number) : number {
    return numero * base;
}

interface PersonajeNuevo {
    nombre : string;
    hp : number;
    mostrarHp : () => void;
}

function curar(personaje : PersonajeNuevo, curar : number) : void {
    personaje.hp += curar;
}

const nuevoPersonaje : PersonajeNuevo = {
    nombre : 'Strider',
    hp : 50,
    mostrarHp() {
        console.log('Puntos de vida: ', this.hp)
    }
}

// curar(nuevoPersonaje, 100)
// const resultado = sumar(10, 20)