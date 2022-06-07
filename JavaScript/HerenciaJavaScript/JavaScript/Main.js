import BombaGasolina from "./BombaGasolina"
import BombaAceite from "./BombaAceite"
import Motor from "./Motor"
import Bateria from "./Bateria"
import Llantas from "./Llantas"
import SistemaFrenos from "./SistemaFrenos"
import AutoMovil from "./Automovil"
import AutoBus from "./Autobus"
import Camioneta from "./Camioneta"
import Mio from "./Mio"
import Furgoneta from "./Furgoneta"
import TractoMula from "./Tractomula"
import Camion from "./Camion"
import Grua from "./Grua"
import Excavadora from "./Excavadora"
import Conductor from "./Conductor"
import Mecanico from "./Mecanico"

let bombaGasolina = new BombaGasolina("Diesel");
let bombaAceite = new BombaAceite("Premium");
let motor = new Motor("AlphaMotores", 2005, 500, bombaGasolina, bombaAceite);
let bateria = new Bateria("Mac", 2003);
let llantas = new Llantas("Michellin", "Lujo");
let sistemaFrenos = new SistemaFrenos("Spartan", "Disco");
let carro = new AutoMovil("Nissan", 2022, 0, 4, 5, motor, bateria, llantas, sistemaFrenos);

let autobus = new AutoBus("Mercedez", 2015, 100, 8, 50);
let camioneta = new Camioneta("Toyota", 2009, 50, 4, 8);
let mio = new Mio("Mercedez", 2004, 200, 8, 60);
let furgoneta = new Furgoneta("Renault", 2006, 30, 4, "50kg");
let tractomula = new TractoMula("Caterpillar", 2008, 500, 10, 8);
let camion = new Camion("Renault", 2010, 600, 8, 10);
let grua = new Grua("Caterpillar", 2020, 2, 2, "Distribuir Cargas");
let excavadora = new Excavadora("Caterpillar", 2021, 3, 2, "Distribuir Cargas");
let conductor = new Conductor("Sebastián", 18, 1105362481, carro);
let mecanico = new Mecanico("Juan", 20, 94515580, carro);


let vehiculos = [
    carro, autobus, camioneta, mio, furgoneta, tractomula, camion, grua, excavadora
];

for(let i = 0; i < vehiculos.length; i++) {
    console.log(vehiculos[i].getMarca());
    console.log(vehiculos[i].getmodelo());
    console.log(vehiculos[i].getKm());
    console.log(vehiculos[i].getCantLlantas());
    console.log("\n");
}

console.log(conductor.getNombre());
console.log(conductor.getVehiculo());