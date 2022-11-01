#include <iostream>
#include <string>

using namespace std;

void numerosEntremedios(int, int);

int main() {
  int num1, num2;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
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

  numerosEntremedios(num1, num2);
} 

void numerosEntremedios(int num1, int num2) {
  int mayor, menor;

  if (num1 > num2) {
    mayor = num1;
    menor = num2;
  } else {
    if (num2 > num1) {
      mayor = num2;
      menor = num1;
    }
  }

  for (int i = menor; i <= mayor; i++) {
    cout << "Número " << i << "\n";
  }
}