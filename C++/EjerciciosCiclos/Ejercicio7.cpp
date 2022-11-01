#include <iostream>
#include <string>
#include <stdlib.h>     
#include <time.h>

using namespace std;

int main() {
  int puntos, num, numrandom, i = 1;
  string nom;
  const int nummax = 5;

  srand (time(NULL));

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  while (i <= nummax) {
    do {
      numrandom = rand() % 20;

      cout << "Número: " << numrandom << "\n";
      cout << "\n";

      cout << nom << " digite un número \n";
      cin >> num;
      cout << "\n";

      if (num != numrandom) {
        cout << "Intentalo otra vez, número incorrecto \n";
        cout << "\n";
      } else {
        if (num == numrandom) {
          cout << "¡Felicidades! número correcto \n";
          cout << "\n";
        }
      }

    } while (num != numrandom);

    i++;
  }
  cout << "¡Felicidades! has ganado";
}