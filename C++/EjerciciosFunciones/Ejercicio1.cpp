#include <iostream>
#include <string>

using namespace std;

void revisar(int, double, double);

int main() {
  string nom;
  int num1;
  double num2, num3; 

  cout << "Autor: Juan Sebastián Dosman \n";
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el primer número \n";
  cin >> num1;
  cout << "\n";
  cout << nom << " digite el segundo número \n";
  cin >> num2;
  cout << "\n";
  cout << nom << " digite el tercer número \n";
  cin >> num3;
  cout << "\n";

  revisar(num1, num2, num3);
}

void revisar(int num1, double num2, double num3) {
  cout << "Número 1: " << num1 << "\n";
  cout << "Número 2: " << num2 << "\n";
  cout << "Número 3: " << num3 << "\n";
}