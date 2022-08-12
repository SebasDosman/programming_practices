/*
    ===== Código de TypeScript =====
*/

import { Producto, calculaISV() } from "./introduccion/DesestructuracionArgumentos";

const carritoCompras : Producto[] = [{
    desc: 'Telefono 1',
    precio: 120
},{
    desc: 'Telefono 2',
    precio: 150
}]

const [total, isv] = calculaISV(carritoCompras)