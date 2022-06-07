export default class Motor {
    constructor(marca, modelo, potencia, bombaGasolina, bombaAceite) {
        this.marca = marca;
        this.modelo = modelo;
        this.potencia = potencia;
        this.bombaGasolina = bombaGasolina;
        this.bombaAceite = bombaAceite;
    }

    getMarca() {
        console.log("Marca Motor: " + this.marca)
    }

    setMarca(marca) {
        this.marca = marca;
    }

    getModelo() {
        console.log("Modelo Motor: " + this.modelo)
    }

    setModelo(modelo) {
        this.modelo = modelo;
    }

    getPotencia() {
        console.log("Potencia Motor: " + this.potencia)
    }

    setPotencia(potencia) {
        this.potencia = potencia;
    }

    getBombaGasolina() {
        console.log("Tipo Gasolina Motor: " + this.bombaGasolina.getTipoGasolina())
    }

    getBombaAceite() {
        console.log("Tipo Aceite Motor: " + this.bombaAceite.getTipoAceite());
    }
}