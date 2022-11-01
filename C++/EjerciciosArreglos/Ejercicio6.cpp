#include <iostream>
#include <string>

using namespace std;

int main() {
  const int tamFilas = 3;
  const int tamColum = 5; 
  double voltajes[tamFilas][tamColum];
  int cont60 = 0, cont70 = 0, cont80 = 0, cont90 = 0, cont100 = 0;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (int i = 0; i < tamFilas; i++) {
    for (int j = 0; j < tamColum; j++) {
      cout << nom << " digite el voltaje número " << j + 1 << " de la ronda " << i + 1 << "\n";
      cin >> voltajes[i][j];
      cout << "\n";
    }
  }

  for (int x = 0; x < tamFilas; x++) {
    for (int y = 0; y < tamColum; y++) {    
      if (voltajes[x][y] < 60) {
        cont60++;
      } else {
        if (voltajes[x][y] >= 60 && voltajes[x][y] < 70) {
          cont70++;
        } else {
          if (voltajes[x][y] >= 70 && voltajes[x][y] < 80) {
            cont80++;
          } else {
            if (voltajes[x][y] >= 80 && voltajes[x][y] < 90) {
              cont90++;
            } else {
              if (voltajes[x][y] > 90) {
                cont100++;
              }
            }
          }
        }
      }
    }
  }

  cout << "Número Total Voltajes: \n";
  cout << "Menores que 60: " << cont60 << "\n";
  cout << "Mayores o iguales que 60 y menores que 70: " << cont70 << "\n";
  cout << "Mayores o iguales que 70 y menores que 80: " << cont80 << "\n";
  cout << "Mayores o iguales que 80 y menores que 90: " << cont90 << "\n";
  cout << "Mayores que 90: " << cont100 << "\n";
}