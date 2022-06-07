export default class SistemaFrenos {
    constructor(marca, tipoFrenos) {
        this.marca = marca;
        this.tipoFrenos = tipoFrenos;
    }

    getMarca() {
        console.log("Marca Sistema De Frenos: " + this.marca);
    }

    setMarca(marca) {
        this.marca = marca;
    }

    getTipoFrenos() {
        console.log("Tipo Frenos: " + this.tipoFrenos)
    }

    setTipoFrenos(tipoFrenos) {
        this.tipoFrenos = tipoFrenos;
    }
}