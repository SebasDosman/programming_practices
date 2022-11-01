#include <iostream>
#include <string>

using namespace std;

int main() {
  int x, y, z, p;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite el valor de X \n";
  cin >> x;
  cout << nom << " digite el valor de Y \n";
  cin >> y;
  cout << nom << " digite el valor de Z \n";
  cin >> z;

  if (x > y && z < 20) {
    cout << nom << " digite el valor de P \n";
    cin >> p;
    cout << "Valor de P: " << p;
  }
}