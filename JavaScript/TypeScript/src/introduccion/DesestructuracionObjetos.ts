interface Reproductor {
    volumen : number;
    segundo : number;
    cancion : string;
    detalles : Detalles;
}

interface Detalles {
    autor : string;
    anio : number;
}

const reproductor : Reproductor = {
    volumen: 90,
    segundo: 36,
    cancion: 'Mess',
    detalles: {
        autor: 'Ed Sheeran',
        anio: 2015,
    }
}

const { volumen, segundo, cancion, detalles : { autor : autorDetalle }} = reproductor;
// const { autor } = detalles;

console.log('El segundo actual de: ', segundo);
console.log('El volumen actual de: ', volumen);
console.log('La canción actual de: ', cancion);
console.log('El autor es: ', autorDetalle);