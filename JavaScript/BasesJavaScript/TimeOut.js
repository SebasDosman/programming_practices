const evaluar = () => {
    const edad = prompt("Cuál es tu edad?");

    if (edad < 18) {
        alert("Eres menor de edad");
        return;
    }

    alert("Eres mayor de edad");
};

setTimeout(evaluar, 2000);