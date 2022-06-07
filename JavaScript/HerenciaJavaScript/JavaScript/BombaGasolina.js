export default class BombaGasolina {
    constructor(tipoGasolina) {
        this.tipoGasolina = tipoGasolina;
    }

    getTipoGasolina() {
        console.log("Tipo Gasolina Bomba Gasolina: " + this.tipoGasolina);
    }

    setTipoGasolina(tipoGasolina) {
        this.tipoGasolina = tipoGasolina;
    }
}