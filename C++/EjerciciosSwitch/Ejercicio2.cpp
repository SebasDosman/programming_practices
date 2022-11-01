#include <iostream>
#include <string>

using namespace std;

int main() {
  int factor;
  double presion;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite el valor del factor \n";
  cin >> factor;

  switch (factor) {
    case 1:
      presion = 25.0;
    break;
    case 2:
      presion = 36.0;
    break;
    case 3:
      presion = 45.0;
    break;
    case 4:
      presion = 49.0;
    break;
    case 5:
      presion = 49.0;
    break;
    case 6:
      presion = 49.0;
    break;
  }
}