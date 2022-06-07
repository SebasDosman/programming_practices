import Vehicle from "../JavaScript/Vehicle";

export default class Remolques extends Vehicle {
    constructor(marca, modelo, km, cantLlantas, cantLlantasRemolque) {
        super(marca, modelo, km, cantLlantas);

        this.cantLlantasRemolque = cantLlantasRemolque;
    }

    getCantLlantasRemolque() {
        console.log("Cant. Llantas Remolque: " + this.cantLlantasRemolque);
    }

    setPesoMercancia(cantLlantasRemolque) {
        this.cantLlantasRemolque = cantLlantasRemolque;
    }
} 