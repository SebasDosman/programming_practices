#include <iostream>
#include <string>

using namespace std;

double Suma (double num1, double num2);
double Resta (double num1, double num2);
double Division (double num1, double num2);
double Multiplicacion (double num1, double num2);

int main() {
  int opcion;
  double num1, num2, suma, resta, multi, divi;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite una de las siguientes opciones \n \n"
    << "Menú: \n"
    << "1. Suma \n" 
    << "2. Resta \n"
    << "3. División \n" 
    << "4. Multiplicación \n";
  cin >> opcion;

  cout << "\n";

  cout << nom << " digite el primer número \n";
  cin >> num1;
  cout << nom << " digite el segundo número \n";
  cin >> num2;
  cout << "\n";

  switch (opcion) {
    case 1:
      suma = Suma(num1, num2);
      cout << nom << " la suma de los dos números es igual a " << suma;
    break;
    case 2:
      resta = Resta(num1, num2);
      cout << nom << " la resta de los dos números es igual a " << resta;
    break;
    case 3:
      divi = Division(num1, num2);

      if (divi != 0) {
        cout << nom << " la división de los dos números es igual a " << divi;
      } else {
        cout << nom << " no se puede realizar una división entre 0";
      }
    break;
    case 4:
      multi = Multiplicacion(num1, num2);
      cout << nom << " la multiplicación de los dos números es igual a " << multi;
    break;
    default:
      cout << nom << " debes digitar un número entre 1 - 4 \n";
  }
}

double Suma (double num1, double num2) {
  double total;

  total = (num1 + num2);

  return total;
}

double Resta (double num1, double num2) {
  double total;

  total = (num1 - num2);

  return total;
}

double Division (double num1, double num2) {
  double total;

  if (num2 != 0) {
    total = (num1 / num2);

    return total;
  } else {
    total = 0;

    return total;
  }
}

double Multiplicacion (double num1, double num2) {
  double total;

  total = (num1 * num2);

  return total;
}