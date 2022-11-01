#include <iostream>
#include <string>

using namespace std;

int main() {
  string nom;
  char genero;
  int i, edad, max, contmasc = 0, contfem = 0, contaptos = 0, nac;

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite la cantidad de personas a evaluar \n";
  cin >> max;
  cout << "\n";

  for (i = 1; i <= max; i++) {
    cout << "Digite su edad \n";
    cin >> edad;
    cout << "\n";

    cout << "¿Es usted de nacionalidad colombiana? \n"
    << "1. Si \n"
    << "2. No \n";
    cin >> nac;
    cout << "\n";

    if (genero != 1 && genero != 2) {
      cout << "Debes digitar una de las opciones \n";
      cout << "\n";
    }
    
    cout << "Digite su genero \n"
    << "M. Masculino \n"
    << "F. Femenino \n";
    cin >> genero;
    cout << "\n";

    if (genero == 'M') {
      contmasc++;
    } else {
      if (genero == 'F') {
        contfem++;
      } else {
        cout << "Debes digitar una de las opciones \n";
        cout << "\n";
      }
    }

    if (edad > 18 && edad < 25 && nac == 1 && genero == 'M') {
      cout << "Eres apto para prestar servicio militar \n";
      contaptos++;
      cout << "\n";
    } else {
      cout << "No eres apto para prestar servicio militar \n";
      cout << "\n";
    }
  }

  cout << nom << " el total de personas evaludas fue " << max << " con un total de " << contfem << " mujeres y " << contmasc << " hombres \n"
  << "Total de hombres aptos: " << contaptos;
}