#include "Perro.h"

Perro::Perro(){}

Perro::Perro(string habitat,string sexo,string nombrePerro,string razaPerro,string sexoPerro,int edadPerro,bool vacunasPerro) : Mamifero(habitat,sexo){  
  this->nombrePerro = nombrePerro;
  this->razaPerro = razaPerro;
  this->sexoPerro = sexoPerro;
  this->edadPerro = edadPerro;
  this->vacunasPerro = vacunasPerro;
}

Perro::~Perro(){}

string Perro::obtenerNombrePerro(){
  return this->nombrePerro;
}

void Perro::actualizarNombrePerro(string nombrePerro){
  this->nombrePerro = nombrePerro;
}

string Perro::obtenerRazaPerro(){
  return this->razaPerro;
}

void Perro::actualizarRazaPerro(string razaPerro){
  this->razaPerro = razaPerro;
}

string Perro::obtenerSexoPerro(){
  return this->sexoPerro;
}

void Perro::actualizarSexoPerro(string sexoPerro){
  this->sexoPerro = sexoPerro;
}

int Perro::obtenerEdadPerro(){
  return this->edadPerro;
}

void Perro::actualizarEdadPerro(int edadPerro){
  this->edadPerro = edadPerro;
}

bool Perro::obtenerVacunasPerro(){
  return this->vacunasPerro;
}

void Perro::actualizarVacunasPerro(bool vacunasPerro){
  this->vacunasPerro = vacunasPerro;
}
