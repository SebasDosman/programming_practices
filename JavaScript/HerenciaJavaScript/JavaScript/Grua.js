import Maquinaria from "../JavaScript/Maquinaria";

export default class Grua extends Maquinaria {
    constructor(marca, modelo, km, cantLlantas, funcionMaquinaria) {
        super(marca, modelo, km, cantLlantas, funcionMaquinaria);
    }

    getMarca() {
        console.log("Marca Grua: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Grua: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Grua: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Grua: " + this.cantLlantas);
    }
}