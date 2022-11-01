#include "Mamifero.h"

Mamifero::Mamifero(){}

Mamifero::Mamifero(string habitat,string sexo){
  this->habitat = habitat;
  this->sexo = sexo;
}

Mamifero::~Mamifero(){}

string Mamifero::obtenerHabitat(){
  return this->habitat;
}    
    
void Mamifero::actualizarHabitat(string habitat){
  this->habitat = habitat;
}

string Mamifero::obtenerSexo(){
  return this->sexo;
}

void Mamifero::actualizarSexo(string sexo){
  this->sexo = sexo;
}
