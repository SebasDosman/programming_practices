export default class Vehicle {
    constructor(marca, modelo, km, cantLlantas) {
        this.marca = marca;
        this.modelo = modelo;
        this.km = km;
        this.cantLlantas = cantLlantas;
    }

    getMarca() {
        console.log("Marca Vehículo: " + this.marca);
    }

    setMarca(marca) {
        this.marca = marca;
    }

    getmodelo() {
        console.log("Modelo Vehículo: " + this.modelo);
    }

    setModelo(modelo) {
        this.modelo = modelo;
    }

    getKm() {
        console.log("Kilometros Vehículo: " + this.km);
    }

    setKm(km) {
        this.km = km;
    }

    getCantLlantas() {
        console.log("Cant. Llantas Vehículo: " + this.cantLlantas);
    }

    setCantLlantas(cantLlantas) {
        this.cantLlantas = cantLlantas;
    }
}