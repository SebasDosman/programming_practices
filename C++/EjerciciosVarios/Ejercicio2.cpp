#include <iostream>
#include <string>

using namespace std;

int main() {
  string nom;
  char opcion; 
  double medida, Cm, Km, In;

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite los metros que desea convertir \n";
  cin >> medida;
  cout << "\n";

  cout << nom << " digite una de las siguientes opciones \n \n"
    << "Menú: \n"
    << "C. Centimetros \n" 
    << "K. Kilometros \n"
    << "P. Pulgadas \n";
  cin >> opcion;

  cout << "\n";

  switch (opcion) {
    case 'C':
      Cm = (medida * 100);
      cout << nom << " " << medida << "m corresponden a " << Cm << "cm";
    break;
    case 'K':
      Km = (medida / 1000);
      cout << nom << " " << medida << "m corresponden a " << Km << "km";
    break;
    case 'P':
      In = (medida * 39.37);
      cout << nom << " " << medida << "m corresponden a " << In << "in";
    break;
    default:
      cout << nom << " debes digitar una opción del menú \n";
  }
}