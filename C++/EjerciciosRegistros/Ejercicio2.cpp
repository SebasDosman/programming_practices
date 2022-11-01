#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

struct Empleados {
  string nombre;
  string direccion;
  string codPostal;
  int salarioNeto;
  string fechaNac;
};

int main() {
  string nom;

  Empleados empleado1;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el nombre del empleado \n";
  cin >> empleado1.nombre;
  cout << "\n";

  cout << nom << " digite la dirección del empleado \n";
  cin >> empleado1.direccion;
  cout << "\n";

  cout << nom << " digite el código postal del empleado \n";
  cin >> empleado1.codPostal;
  cout << "\n";

  cout << nom << " digite el salario neto del empleado \n";
  cin >> empleado1.salarioNeto;
  cout << "\n";

  cout << nom << " digite la fecha de nacimiento del empleado \n";
  cin >> empleado1.fechaNac;
  cout << "\n";

  cout << "Nombre \t \t" << "Dirección \t \t"  << "Código Postal \t \t" << "Salario Neto \t \t" << "Fecha Nacimiento" << "\n";
  cout << "------------------------------------------------------------------------------------";
  cout << "\n";
  cout << empleado1.nombre << setw(14) << empleado1.direccion << setw(16) << empleado1.codPostal << setw(19) << empleado1.salarioNeto << setw(20) << empleado1.fechaNac << endl; 
} 