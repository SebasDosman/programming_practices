#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

void selTab(int, int, int);

int main() {
  string nom;
  int num1, num2, num3;

  cout << "Autor: Juan Sebastián Dosman \n";
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el valor inicial de la tabla \n";
  cin >> num1;
  cout << "\n";
  cout << nom << " digite el número de valores a desplegar \n";
  cin >> num2;
  cout << "\n";
  cout << nom << " digite el incremento entre valores \n";
  cin >> num3;
  cout << "\n";

  selTab(num1, num2, num3);
}

void selTab(int num1, int num2, int num3 = 1) {
  int incremento = num1;

  cout << "Tabla de incrementos \n";
  cout << "-------------------- \n";

  for (int i = 1; i <= num2; i++) {
    cout << setw(10) << incremento << "\n";
    incremento += num3;
  }
}