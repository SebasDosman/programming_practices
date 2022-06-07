import TransportePasajeros from "../JavaScript/TransportePasajeros";

export default class Camioneta extends TransportePasajeros {
    constructor(marca, modelo, km, cantLlantas, cantPasajeros) {
        super(marca, modelo, km, cantLlantas, cantPasajeros);
    }

    getMarca() {
        console.log("Marca Camioneta: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Camioneta: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Camioneta: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Camioneta: " + this.cantLlantas);
    }
}