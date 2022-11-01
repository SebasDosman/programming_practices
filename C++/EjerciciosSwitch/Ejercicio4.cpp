#include <iostream>
#include <string>

using namespace std;

int main() {
  char codigo;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " introduzca el código de especificación \n";
  cin >> codigo;

  switch (codigo) {
    case 'S':
      cout << nom << " el elemento tiene grado de exploración espacial \n";
    break;
    case 'M':
      cout << nom << " el elemento tiene grado militar \n";
    break;
    case 'C':
      cout << nom << " el elemento tiene grado comercial \n";
    break;
    case 'T':
      cout << nom << " el elemento tiene grado de juguete \n";
    break;
    default:
      cout << nom << " se ha introducido un código invalido \n";
  }
}