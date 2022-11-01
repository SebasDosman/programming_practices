#include <iostream>
#include <string>

using namespace std;

int main() {
  const int tamañoVoltios = 9;
  double voltios[tamañoVoltios];
  int i, j;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (i = 0; i < sizeof(voltios) / sizeof(voltios[tamañoVoltios]); i++) {
    cout << nom << " digite el valor en voltios de la posición " << i + 1 << "\n";
    cin >> voltios[i];
    cout << "\n";
  }

  for (j = 0; j < sizeof(voltios) / sizeof(voltios[tamañoVoltios]); j++) {
    cout << "Valor " << j + 1  << ": " << voltios[j] << "\n";
  }
}