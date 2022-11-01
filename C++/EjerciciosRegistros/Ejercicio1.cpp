#include <iostream>
#include <string>

using namespace std;

struct Paciente {
  string nom;
  string ape;
  int edad;
  char sexo;
  double temp;
};

int main() {
  Paciente pac1;

  pac1 = {
    "Carlos",
    "Restrepo",
    18,
    'M',
    37.8
  };

  cout << "Nombre: " <<  pac1.nom << "\n";
  cout << "Apellido: " <<  pac1.ape << "\n";
  cout << "Edad: " <<  pac1.edad << "\n";
  cout << "Sexo: " <<  pac1.sexo << "\n";
  cout << "Temperatura: " <<  pac1.temp << "\n";
} 