#include <iostream>
#include <string>

using namespace std;

int main() {
  string nom;
  int iva, km, kmtotal, montototal;
  const int montofijo300 = 300000;
  const int montofijo1000 = 10500000;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite la cantidad de kilometros recorridos \n";
  cin >> km;
  cout << "\n";

  if (km <= 300) {
    montototal = montofijo300;
  } else {
    if (km > 300 && km <= 1000) {
      kmtotal = (km - 300);
      montototal = ((kmtotal * 15000) + montofijo300);
    } else {
      if (km > 1000) {
        kmtotal = (km - 1000);
        montototal = ((kmtotal * 10000) + montofijo300 + montofijo1000);
      }
    }
  }

  iva = (montototal * 0.20);
  montototal += iva;

  cout << nom << " el total a pagar es $" << montototal << " con un iva de $" << iva << " incluido";
}
