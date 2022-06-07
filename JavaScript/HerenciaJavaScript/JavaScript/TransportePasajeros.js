import Vehicle from "../JavaScript/Vehicle";

export default class TransportePasajeros extends Vehicle {
    constructor(marca, modelo, km, cantLlantas, cantPasajeros) {
        super(marca, modelo, km, cantLlantas);

        this.cantPasajeros = cantPasajeros;
    }

    getCantPasajeros() {
        console.log("Cant Pasajeros: " + this.cantPasajeros);
    }

    setCantPasajeros(cantPasajeros) {
        this.cantPasajeros = cantPasajeros;
    };
}