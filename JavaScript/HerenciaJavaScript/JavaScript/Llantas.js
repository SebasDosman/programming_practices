export default class Llantas {
    constructor(marca, tipoRin) {
        this.marca = marca;
        this.tipoRin = tipoRin;
    }

    getMarca() {
        console.log("Marca Llantas: " + this.marca);
    }

    setMarca(marca) {
        this.marca = marca;
    }

    getTipoRin() {
        console.log("Tipo Rin: " + this.tipoRin);
    }

    setTipoRin(tipoRin) {
        this.tipoRin = tipoRin;
    }
}