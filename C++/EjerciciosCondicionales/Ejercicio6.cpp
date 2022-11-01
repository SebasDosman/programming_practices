#include <iostream>
#include <string>

using namespace std;

int main() {
  int frecuencia;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite la frecuencia \n";
  cin >> frecuencia;

  if (frecuencia > 60) {
    cout << nom << " la frecuencia es demasiado alta \n";
  } 
}