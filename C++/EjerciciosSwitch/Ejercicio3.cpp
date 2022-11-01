#include <iostream>
#include <string>

using namespace std;

int main() {
  string nom;
  int cod;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite el código \n";
  cin >> cod;

  switch (cod) {
    case 1:
      cout << "Fabricante de Unidad de Disco: 3M Corporation \n";
    break;
    case 2:
      cout << "Fabricante de Unidad de Disco: Maxell Corporation \n";
    break;
    case 3:
      cout << "Fabricante de Unidad de Disco: Sony Corporation \n";
    break;
    case 4:
      cout << "Fabricante de Unidad de Disco: Verbatin Corporation \n";
    break;
  }
}