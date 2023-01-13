// const saludo = async() => { 
//     resolve("Hola Mundo");
// };

// saludo().then((res) => console.log(res));

const peticion = async() => {
    setTimeout(() => {
        const datos = {
            id: 1,
            nombre: "Juan",
            apellido: "Perez"
        };

        console.log(datos);
    }, 1000);
};

peticion();