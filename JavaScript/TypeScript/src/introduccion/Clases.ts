class PersonaNormal {
    constructor (
       public nombre : String,
       public direccion : String
    ) { }
}

class Heroe extends PersonaNormal {
   constructor (
       public alterEgo : String, 
       public edad : number, 
       public nombrereal : String
   ) { 
       super ( nombrereal, "New York, USA" )
   }
}

const ironman = new Heroe("Iron Man", 15, "Tony");

console.log(ironman); 