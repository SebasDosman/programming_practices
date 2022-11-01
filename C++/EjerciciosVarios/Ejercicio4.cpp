#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
  int opcion;
  double base, altura, area, perimetro, lado1, lado2, radio;
  const double pi = 3.1614;
  string nom;
  
  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";
  
  cout << nom << " digite una de las siguientes opciones \n \n"
    << "Menú: \n"
    << "1. Área y perímetro de un rectángulo \n" 
    << "2. Área y perímetro de un triangulo \n"
    << "3. Área y perímetro de un circulo \n";
  cin >> opcion;

  cout << "\n";

  switch (opcion) {
    case 1:
      cout << nom << " digite la base del rectángulo \n";
      cin >> base;
      cout << nom << " digite la altura del rectángulo \n";
      cin >> altura;
      cout << "\n";

      area = (base * altura);
      perimetro = ((base * 2) + (altura * 2));

      cout << nom << " el área del rectángulo es " << area << " y el perímetro es " << perimetro;
    break;
    case 2:
      cout << nom << " digite la base del triangulo \n";
      cin >> base;
      cout << nom << " digite el segundo lado del triangulo \n";
      cin >> lado1;
      cout << nom << " digite el tercer lado del triangulo \n";
      cin >> lado2;
      cout << nom << " digite la altura del triangulo \n";
      cin >> altura;
      cout << "\n";

      area = (base * altura) / 2;
      perimetro = (base + lado1 + lado2);

      cout << nom << " el área del triangulo es " << area << " y el perímetro es " << perimetro;
    break;
    case 3:
      cout << nom << " digite el radio del circulo \n";
      cin >> radio;
      cout << "\n";

      area = (pi * pow(radio, 2));
      perimetro = ((2 * pi) * radio);

      cout << nom << " el área del circulo es " << area << " y el perímetro es " << perimetro;
    break;
    default:
      cout << nom << " debes digitar un número entre 1 - 3 \n";
  }
}