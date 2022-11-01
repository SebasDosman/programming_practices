#include <iostream>
#include <string>

using namespace std;

int main() {
  double pendiente, flag;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite la pendiente \n";
  cin >> pendiente;

  if (pendiente < 0.5) {
    flag = 0;
    cout << "Valor de flag: " << flag << "\n";
  } else {
    flag = 1;
    cout << "Valor de flag: " << flag << "\n";
  }
}