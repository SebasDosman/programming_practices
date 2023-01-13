/*
    Tarea: De acuerdo con las siguientes variables, simular la creacion de un usuario
    con las siguientes validaciones:
    1. Validar todas las variables de tipo cadena no sean nulas, y que no esten vacias
    2. Validar que el password coincida con password_confirm
    3. Validar acepte los terminos
    Si todas las validaciones son verdaderas, crear una variable de tipo objeto,
    cuyos atributos sean las variables evaluadas.
    NOTA: Debe implementar funciones para al menos una validacion y usarla correctamente
*/

let full_name = "Fulanito de tal";
let username = "fulanito123";
let email = "email@example.com";
let password = "123isu";
let password_confirm = "123isu";
let acept_terms = false;

function Validacion(User) {
    if (condicion1 == true && condicion2 == true && condicion3 == true){
        for (const j in User) {
            console.log(j+" : "+User[j]);
        }
    } else {
        console.log("No es posible crear el usuario, no se cumple alguna de las condiciones");
    }
}

var User = {
    full_name,
    username,
    email,
    password,
    password_confirm,
    acept_terms
}

for (const i in User) {
    if (User[i] !== "" && User[i] != null) {
        console.log("Cumple las condiciones");
        var condicion1 = true;
    } if (User[i] === "" || User[i] === null)  {
        console.log("No cumple las condiciones");
        var condi = 0;
        condi++;
    }
}
if (condi >= 1) {
    var condicion1 = false;
} 
console.log(" ");  

if (User.password == User.password_confirm) {
    var condicion2 = true;
    console.log("La contraseña es correcta");
} else {
    var condicion2 = false;
    console.log("La contraseña es incorrecta");
}
console.log(" ");

if (User.acept_terms) {
    var condicion3 = true;
    console.log("Aceptó los terminos")
} else {
    var condicion3 = false;
    console.log("No aceptó los terminos");
}
console.log(" ");

return Validacion(User);