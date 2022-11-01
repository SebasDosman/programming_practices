#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
  int año, depreciacion = 0, acuDepreciacion = 0, valorFinal, dolar;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite los años a calcular la depreciación del dolar \n";
  cin >> año;
  cout << "\n";

  cout << nom << " digite el valor de depreciación \n";
  cin >> depreciacion;
  cout << "\n";

  cout << nom << " digite el valor del dolar en el que desea comenzar a hacer la depreciación \n";
  cin >> dolar;
  cout << "\n";

  cout << "Año" << "\t \t" << "Depreciación" << "\t" << "Valor Final Año" << "\t \t" << "Depreciación Acumulada" << "\n";
  cout << "-------------------------------------------------------------------";
  cout << "\n";

  acuDepreciacion = depreciacion;
  valorFinal = dolar;

  for (int i = 1; i <= año && valorFinal >= 0; i++) {
    cout << i << setw(15) << depreciacion << setw(17) << valorFinal << setw(25) << acuDepreciacion << "\n";

    dolar -= depreciacion;
    valorFinal = dolar;

    acuDepreciacion += depreciacion;
  }
}