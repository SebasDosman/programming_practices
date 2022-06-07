import Remolques from "../JavaScript/Remolques";

export default class TractoMula extends Remolques {
    constructor(marca, modelo, km, cantLlantas, cantLlantasRemolque) {
        super(marca, modelo, km, cantLlantas, cantLlantasRemolque);
    }

    getMarca() {
        console.log("Marca Tractomula: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Tractomula: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Tractomula: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Tractomula: " + this.cantLlantas);
    }
}