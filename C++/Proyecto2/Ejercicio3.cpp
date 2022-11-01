#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
  const int tamFilas = 5;
  const int tamColum = 5;
  float numeros[tamFilas][tamColum], sumatoria[tamFilas], promedio[tamFilas], num, suma = 0, suma2 = 0, prom;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (int a = 0; a < tamFilas; a++) {
    for (int b = 0; b < tamColum; b++) {
      cout << nom << " digite el valor número " << b + 1 << " de la posición " << a + 1 << "\n";
      cin >> num;
      numeros[a][b] = num;
      cout << "\n";
    }
  }

  for (int i = 0; i < tamFilas; i++) {
    suma = 0;
    for (int d = 0; d < tamColum; d++) {
      suma += numeros[i][d];
    }
    sumatoria[i] = suma; 
  }

  for (int x = 0; x < tamFilas; x++) {
    suma2 = 0;
    for (int y = 0; y < tamColum; y++) {
      suma2 += numeros[x][y];
    }
    prom = (suma2 / tamFilas);
    promedio[x] = prom; 
  }

  for (int j = 0; j < tamColum; j++) {
    cout << setw(7) << j << setw(10);
  }
  cout << setw(10) << "Suma" << setw(11) << "Promedio" << "\n";
  cout << "----------------------------------------------------------";
  cout << "\n";

  for (int c = 0; c < tamFilas; c++) {
    cout << c;
    for (int e = 0; e < tamColum; e++) {
      cout << "\t" << numeros[c][e] << setw(5);
    }
    cout << setw(7) << sumatoria[c] << setw(8) << promedio[c];
    cout << "\n";
  }
}