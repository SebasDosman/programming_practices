// let mensaje = "";

// if (cuenta < 0) mensaje = "No tienes saldo";
// else mensaje = "Tienes saldo";

const cuenta = 10;

const mensaje = cuenta < 0 ? "No tienes saldo" : "Tienes saldo";
const mensaje1 = cuenta < 0 && "No tienes saldo";

document.write(mensaje);