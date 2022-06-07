import TransportePasajeros from "../JavaScript/TransportePasajeros";

export default class AutoMovil extends TransportePasajeros {
    constructor(marca, modelo, km, cantLlantas, cantPasajeros, motor,  bateria, llantas, sistemaFrenos) {
        super(marca, modelo, km, cantLlantas, cantPasajeros);

        this.motor = motor;
        this.bateria = bateria;
        this.llantas = llantas;
        this.sistemaFrenos = sistemaFrenos;
    }

    getMarca() {
        console.log("Marca Automovil: " + this.marca);
    }

    getmodelo() {
        console.log("Modelo Automovil: " + this.modelo);
    }

    getKm() {
        console.log("Kilometros Automovil: " + this.km);
    }

    getCantLlantas() {
        console.log("Cant. Llantas Automovil: " + this.cantLlantas);
    }

    getMotor() {
        console.log("Motor Automovil: " + this.motor.getMarca());
    }

    getBateria() {
        console.log("Bateria Automovil: " + this.bateria.getMarca());
    }

    getLlantas() {
        console.log("Llantas Automovil: " + this.llantas.getMarca())
    }

    getSistemaFrenos() {
        console.log("Sistema De Frenos Automovil: " + this.sistemaFrenos.getMarca());
    }
}