#include <iostream>
#include <string>

using namespace std;

int main() {
  int voltios, tiempo;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite el tiempo en segundos\n";
  cin >> tiempo;

  if (tiempo < 2) {
    voltios = 0;
    cout << "Valor en voltio de la ondas: " << voltios << "\n";
  } else {
    if (tiempo >= 2) {
      voltios = 3;
      cout << "Valor en voltios de la onda: " << voltios << "\n";
    }
  }
}