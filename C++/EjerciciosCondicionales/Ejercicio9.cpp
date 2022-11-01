#include <iostream>
#include <string>

using namespace std;

int main() {
  int distancia, tiempo;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite el valor de la distancia \n";
  cin >> distancia;

  if (distancia > 20 && distancia < 35) {
    cout << nom << " digite el valor del tiempo \n";
    cin >> tiempo;
    cout << "Valor del tiempo: " << tiempo;
  }
}