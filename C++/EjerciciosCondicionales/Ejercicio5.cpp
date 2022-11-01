#include <iostream>
#include <string>

using namespace std;

int main() {
  double voltios1, voltios2, resta, aprox;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite la primer cantidad de voltios \n";
  cin >> voltios1;
  cout << nom << " digite la segunda cantidad de voltios \n";
  cin >> voltios2;

  resta = (voltios1 - voltios2);

  if (resta < 0.001) {
    aprox = 0;
    cout << "Valor de aprox: " << aprox << "\n";
  } else {
    aprox = (voltios1 - voltios2) / 2;
    cout << "Valor de aprox: " << aprox << "\n";
  }
}