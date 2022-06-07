import Maquinaria from "../JavaScript/Maquinaria";

export default class Excavadora extends Maquinaria {
    constructor(marca, modelo, km, cantLlantas, funcionMaquinaria) {
        super(marca, modelo, km, cantLlantas, funcionMaquinaria);
    }

    getMarca() {
        console.log("Marca Excavadora: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Excavadora: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Excavadora: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Excavadora: " + this.cantLlantas);
    }
}