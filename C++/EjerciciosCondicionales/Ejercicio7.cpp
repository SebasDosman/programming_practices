#include <iostream>
#include <string>

using namespace std;

int main() {
  double temp1, temp2, resta, error, factor = 0.5;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite la primera temperatura \n";
  cin >> temp1;
  cout << nom << " digite la segunda temperatura \n";
  cin >> temp2;

  resta = (temp1 - temp2);

  if (resta > 2.3) {
    error = (temp1 - temp2) * factor;
    cout << "Valor de error: " << error << "\n";
  } 
}