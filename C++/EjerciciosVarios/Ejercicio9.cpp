#include <iostream>
#include <string>

using namespace std;

int main() {
  double nota;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << "\n";

  cout << nom << " digite su nota \n";
  cin >> nota;

  cout << "\n";

  if (nota >= 0 && nota <= 5.9) {
    cout << nom << " su nota corresponde a la letra D \n";
  } else {
    if (nota >= 6 && nota <= 6.9) {
      cout << nom << " su nota corresponde a la letra A \n";
    } else {
      if (nota >= 7 && nota <= 7.9) {
        cout << nom << " su nota corresponde a la letra B \n";
      } else {
        if (nota >= 8 && nota <= 8.9) {
          cout << nom << " su nota corresponde a la letra S \n";
        } else {
          if (nota >= 9 && nota <= 10) {
            cout << nom << " su nota corresponde a la letra E \n";
          } else {
            cout << nom << " debes digitar una nota entre 0 - 10";
          }
        }
      }
    }
  }
}