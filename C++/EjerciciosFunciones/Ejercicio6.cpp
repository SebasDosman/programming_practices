#include <iostream>
#include <math.h>
#include <string>
#include <ctype.h>

using namespace std;

void calculoCilindro(double, double);

int main() {
  string nom;
  double radio, altura;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el radio del cilindro \n";
  cin >> radio;
  cout << "\n";

  cout << nom << " digite la altura del clindro \n";
  cin >> altura;
  cout << "\n";

  calculoCilindro(radio, altura);
} 

void calculoCilindro(double radio, double altura) {
  char opcion;
  double area, volumen;

  cout << "Digite Volumen(v) o Área(a) \n";
  cin >> opcion;
  cout << "\n";

  opcion = tolower(opcion);

  switch (opcion) {
    case 'v':
      volumen = (3.1416 * pow(radio, 2)) * altura;
      cout << "El volumen corresponde a " << volumen << "m³" << "\n";
    break;
    case 'a':
      area = (2 * 3.1416 * radio * altura) + (2 * 3.1416 * pow(radio, 2));
      cout << "El área corresponde a " << area << "m²" << "\n";
    break;
    default:
      cout << "Debes digitar un valor correspondiente \n";
  }
}