import Vehicle from "../JavaScript/Vehicle";

export default class TransporteMercancias extends Vehicle {
    constructor(marca, modelo, km, cantLlantas, pesoMercancia) {
        super(marca, modelo, km, cantLlantas);

        this.pesoMercancia = pesoMercancia;
    }

    getPesoMercancia() {
        console.log("Peso Mercancía: " + this.pesoMercancia);
    }

    setPesoMercancia(pesoMercancia) {
        this.pesoMercancia = pesoMercancia;
    }
} 