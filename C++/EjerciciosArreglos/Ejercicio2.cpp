#include <iostream>
#include <string>

using namespace std;

int main() {
  const int tamañoTemp = 8;
  int temp[tamañoTemp], i , j;
  double prom, total;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (i = 0; i < sizeof(temp) / sizeof(temp[tamañoTemp]); i++) {
    cout << nom << " digite el número " << i + 1 << "\n";
    cin >> temp[i];
    cout << "\n";

    total += temp[i];
  }

  for (j = 0; j < sizeof(temp) / sizeof(temp[tamañoTemp]); j++) {
    cout << "Valor " << j + 1 << ": " << temp[j] << "\n";
  }

  cout << "\n";

  prom = (total / (sizeof(temp) / sizeof(temp[tamañoTemp])));

  cout << nom << " el promedio de los valores ingresados correpsonde a " << prom;
}