export default class Bateria {
    constructor(marca, modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }

    getMarca() {
        console.log("Marca Batería: " + this.marca);
    }

    setMarca(marca) {
        this.marca = marca;
    }

    getModelo() {
        console.log("Modelo Batería: " + this.modelo);
    }

    setModelo(modelo) {
        this.modelo = modelo;
    }
}