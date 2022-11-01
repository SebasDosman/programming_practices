#include <iostream>
#include <string>

using namespace std;

void mult(float, float);

int main() {
  string nom;
  float num1, num2;

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

  mult(num1, num2);
}

void mult(float num1, float num2) {
  float result = 0;

  result = (num1 * num2);

  cout << "Resultado: " << result;
}