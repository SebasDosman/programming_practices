#include <iostream>
#include <string> 
using namespace std;

int main() {
  int grados;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite los grados del ángulo \n";
  cin >> grados;

  if (grados == 90) {
    cout << nom << " el ángulo es un ángulo recto \n";
  } else {
    cout << nom << " el ángulo no es un ángulo recto \n";
  }
}