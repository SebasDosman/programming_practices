function classDecorator<T extends { new (...args : any[]): {} }> (constructor : T) {
    return class extends constructor {
        newProperty = "new property";
        hello = "override";
    };
};

@classDecorator
class MiSuperClase {
    private miPropiedad : String = "ABC123";

    imprimir() {
        console.log("Hola Mundo")
    }
}

console.log(MiSuperClase)