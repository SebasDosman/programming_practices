#include <iostream>
#include <string>

using namespace std;

int main() {
  long double fact = 1;
  int num, i;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el número para calcular su factorial \n";
  cin >> num;
  cout << "\n";

  if (num > 0) {
    for (i = 1; i <= num; i++) {
      fact *= i;
    }

    cout << nom << " el factorial del número " << num << " corresponde a " << fact;
  } else {
    if (num == 0) {
      cout << nom << " el factorial del número " << num << " corresponde a " << fact;
    } else {
      cout << nom << " debes ingresar un número positivo";
    }
  }
}
