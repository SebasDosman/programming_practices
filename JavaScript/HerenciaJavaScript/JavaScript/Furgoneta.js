import TransporteMercancias from "../JavaScript/TransporteMercancias"; 

export default class Furgoneta extends TransporteMercancias {
    constructor(marca, modelo, km, cantLlantas, pesoMercancia) {
        super(marca, modelo, km, cantLlantas, pesoMercancia);
    }

    getMarca() {
        console.log("Marca Furgoneta: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Furgoneta: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Furgoneta: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Furgoneta: " + this.cantLlantas);
    }
}