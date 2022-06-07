export default class Mecanico {
    constructor(nombre, edad, cedula, vehiculo) {
        this.nombre = nombre;
        this.edad = edad;
        this.cedula = cedula;
        this.vehiculo = vehiculo;
    }

    getNombre() {
        console.log("Nombre: " + this.nombre);
    }

    setNombre(nombre) {
        this.nombre = nombre;
    }

    getEdad() {
        console.log("Edad: " + this.edad);
    }

    setEdad(edad) {
        this.edad = edad;
    }

    getCedula() {
        console.log("Cédula: " + this.cedula);
    }

    setCedula(cedula) {
        this.cedula = cedula;
    }

    getVehiculo() {
        console.log("Vehículo: " + this.vehiculo.getMarca());
    }
}