import Remolques from "../JavaScript/Remolques";

export default class Camion extends Remolques {
    constructor(marca, modelo, km, cantLlantas, cantLlantasRemolque) {
        super(marca, modelo, km, cantLlantas, cantLlantasRemolque);
    }

    getMarca() {
        console.log("Marca Camión: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Camión: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Camión: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Camión: " + this.cantLlantas);
    }
}