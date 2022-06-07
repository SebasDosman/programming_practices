import TransportePasajeros from "../JavaScript/TransportePasajeros";

export default class AutoBus extends TransportePasajeros {
    constructor(marca, modelo, km, cantLlantas, cantPasajeros) {
        super(marca, modelo, km, cantLlantas, cantPasajeros);
    }

    getMarca() {
        console.log("Marca Autobus: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Autobus: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Autobus: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Autobus: " + this.cantLlantas);
    }
}