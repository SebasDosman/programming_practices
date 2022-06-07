import Vehicle from "../JavaScript/Vehicle";

export default class Maquinaria extends Vehicle {
    constructor(marca, modelo, km, cantLlantas, funcionMaquinaria) {
        super(marca, modelo, km, cantLlantas);

        this.funcionMaquinaria = funcionMaquinaria;
    }

    getFuncionMaquinaria() {
        console.log("Función Maquinaría: " + this.funcionMaquinaria);
    }

    setFuncionMaquinaria(funcionMaquinaria) {
        this.funcionMaquinaria = funcionMaquinaria;
    }
}