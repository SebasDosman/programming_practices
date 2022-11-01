#include "main.h"

int main() {

  Perro objeto = solicitarDatos(); 

  imprimirObjeto(objeto);

  //objeto.~Perro();

  return 0;
}

void imprimirObjeto(Perro objeto){
  cout << objeto.obtenerNombrePerro()  << endl ;
  cout << objeto.obtenerRazaPerro()  << endl ;
  cout << objeto.obtenerSexoPerro()  << endl ;
  cout << objeto.obtenerEdadPerro()  << endl ;
  if (objeto.obtenerVacunasPerro()) {
    cout << "Está vacunado" << endl;
  } else {
    cout << "No está vacunado" << endl;
  }
  cout << objeto.obtenerHabitat() << endl;
  cout << objeto.obtenerSexo() << endl;
}

Perro solicitarDatos(){
  Perro miObjeto = Perro();

  string nombre="";
  string raza="";
  string sexo="";
  int edad =0;
  bool vacunas;

  cout << "Ingrese el nombre del perro: "; 
  getline (cin,nombre);
  cout << "Ingrese la raza del perro: "; 
  getline (cin,raza);
  cout << "Ingrese el sexo del perro: "; 
  getline (cin,sexo);
  cout << "Ingrese la edad del perro: ";
  cin >> edad;
  cout << "Ingrese el siguiente número si su perro está o no está vacunado: \n 1. Si \n 0. No: ";
  cin >> vacunas;

  miObjeto.actualizarNombrePerro(nombre);
  miObjeto.actualizarRazaPerro(raza);
  miObjeto.actualizarSexoPerro(sexo);
  miObjeto.actualizarEdadPerro(edad);
  miObjeto.actualizarVacunasPerro(vacunas);
  miObjeto.actualizarHabitat("Casa");
  miObjeto.actualizarSexo("Canis lupus familiaris");

  return miObjeto;
}