import TransportePasajeros from "../JavaScript/TransportePasajeros";

export default class Mio extends TransportePasajeros {
    constructor(marca, modelo, km, cantLlantas, cantPasajeros) {
        super(marca, modelo, km, cantLlantas, cantPasajeros);
    }

    getMarca() {
        console.log("Marca Mío: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Mío: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Mío: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Mío: " + this.cantLlantas);
    }
}