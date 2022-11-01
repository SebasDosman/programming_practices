#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  const int tamFilas1 = 2;
  const int tamColum1 = 3;
  int primero[tamFilas1][tamColum1] = {{16, 18, 23}, 
                                      {54, 91, 11}};
  const int tamFilas2 = 2;
  const int tamColum2 = 3;
  int segundo[tamFilas2][tamColum2] = {{24, 52, 77},
                                      {16, 19, 59}};
  const int tamFilas3 = 2;
  const int tamColum3 = 3;                                int resultante[tamFilas3][tamColum3], suma;  
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";     

  for (int i = 0; i < tamFilas3; i++) {
    for (int j = 0; j < tamColum3; j++) {
      suma = (primero[i][j] + segundo[i][j]);
      resultante[i][j] = suma;
    }
  }

  cout << setw(11) << "Primero \n";
  cout << "------------ \n";

  for (int x = 0; x < tamFilas3; x++) {
    for (int y = 0; y < tamColum3; y++) {
      cout << " " << primero[x][y] << "\t";
    }
    cout << "\n";
  }

  cout << "\n";
  cout << setw(11) << "Segundo \n";
  cout << "------------ \n";

  for (int a = 0; a < tamFilas3; a++) {
    for (int b = 0; b < tamColum3; b++) {
      cout << " " << segundo[a][b] << "\t";
    }
    cout << "\n";
  }

  cout << "\n";
  cout << setw(15) << "Resultante \n";
  cout << " " << "-------------- \n";

  for (int c = 0; c < tamFilas3; c++) {
    for (int d = 0; d < tamColum3; d++) {
      cout << "  " << resultante[c][d];
    }
    cout << "\n";
  }
}