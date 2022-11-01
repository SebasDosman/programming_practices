#include <iostream>
#include <string>

using namespace std;

int main() {
  int opcion;
  double temp, centigrados, farenheit; 
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite los grados a convertir \n";
  cin >> temp;
  cout << "\n";
  
  cout << nom << " digite una de las siguientes opciones \n \n"
    << "Menú: \n"
    << "1. De grados centígrados a Farenheit \n" 
    << "2. De grados Farenheit a centígrados \n";
  cin >> opcion;

  cout << "\n";

  switch (opcion) {
    case 1:
      centigrados = (9/5 * temp) + 32;
      cout << nom << " " << temp << " grados centígrados corresponden a " << centigrados << " grados Farenheit";
    break;
    case 2:
      farenheit = (temp - 32) * 5/9;
      cout << nom << " " << temp << " grados Farenheit corresponden a " << farenheit << " grados Farenheit";
    break;
    default:
      cout << nom << " debes digitar un número entre 1 - 2 \n";
  }
}