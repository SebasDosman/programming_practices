#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
  const int tamañoCalif = 14;
  const int tamañoDesv = 14;
  int calificaciones[tamañoCalif], i , j, z;
  double desviaciones[tamañoDesv];
  double prom = 0, total = 0, desviacion = 0;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (i = 0; i < sizeof(calificaciones) / sizeof(calificaciones[tamañoCalif]); i++) {
    cout << nom << " digite el número " << i + 1 << "\n";
    cin >> calificaciones[i];
    cout << "\n";

    total += calificaciones[i];
  }

  prom = (total / (sizeof(calificaciones) / sizeof(calificaciones[tamañoCalif])));

  for (j = 0; j < sizeof(calificaciones) / sizeof(calificaciones[tamañoCalif]); j++) {
    desviacion = (calificaciones[j] - prom);

    desviaciones[j] = desviacion;
  }

  cout << setw(12) << "Valores" << setw(20) << "Desviaciones \n";
  cout << "\n";

  for (z = 0; z < sizeof(calificaciones) / sizeof(calificaciones[tamañoCalif]); z++) {
    cout << setw(10) << calificaciones[z] << setw(20) << desviaciones[z] << "\n";
  }

  cout << "\n";
  cout << nom << " el promedio de los valores ingresados correpsonde a " << prom;
}