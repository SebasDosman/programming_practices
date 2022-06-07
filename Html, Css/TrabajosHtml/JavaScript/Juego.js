var Vida = 100;
/* var Ataque = 10;
var Pocion = 20; */

function ataqueEnemigo (Potencia, nombreAtaque) {
    Vida -= Potencia;
    console.log("Has sido atacado con: "+nombreAtaque);
    muestreVida(Vida);
}

function bebePocion (Pocion, tipoPocion) {
    Vida += Pocion;
    console.log("Has tomado una poción llamada: "+tipoPocion);
    muestreVida(Vida);
}

function muestreVida (Vida) {
    console.log("El nivel de vida del personaje es: "+Vida);
}


