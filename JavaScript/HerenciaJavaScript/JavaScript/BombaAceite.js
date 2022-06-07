export default class BombaAceite {
    constructor(tipoAceite) {
        this.tipoAceite = tipoAceite;
    }

    getTipoAceite() {
        console.log("Tipo Aceite Bomba Aceite: " + this.tipoAceite);
    }

    setTipoAceite(tipoAceite) {
        this.tipoAceite = tipoAceite;
    }
}