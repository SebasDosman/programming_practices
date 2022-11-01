#include <iostream>
#include <string>

using namespace std;

int main() {
  string nom, cod;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite el código \n";
  cin >> cod;

  if (cod == "s") {
    cout << nom << " debes usar el generador de 20 kilowatts \n";
  } else {
    cout << nom << " debes usar el generador de 50 kilowatts \n";
  }
}