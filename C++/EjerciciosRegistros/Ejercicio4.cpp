#define maxJugadores 10

#include <iostream>
#include <string>

using namespace std;

struct listaJugadores {
  string nombre;
  int edad;
  double altura;
};

int main() {
  string nom;
  int opcion;

  listaJugadores jugador[maxJugadores];

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (int i = 0; i < maxJugadores; i++) {
    cout << nom << " digite el nombre del jugador " << i+ 1 << endl;
    cin >> jugador[i].nombre;
    cout << "\n";

    cout << nom << " digite la edad del jugador " << i + 1 << endl;
    cin >> jugador[i].edad;
    cout << "\n";

    cout << nom << " digite la altura del jugador " << i + 1 << endl;
    cin >> jugador[i].altura;
    cout << "\n";
  }

  do {
    cout << "Menú: \n"
    << "1. Listar por nombres de jugadores \n"
    << "2. Listar por alturas de jugadores \n"
    << "3. Listar por edades de jugadores \n"
    << "4. Salir \n";
    cin >> opcion;
    cout << "\n";

    switch (opcion) {
    case 1:
      cout << "Nombres \n";
      cout << "------- \n";

      for (int a = 0; a < maxJugadores; a++) {
        cout << jugador[a].nombre << endl;
      }

      cout << "\n";
    break;
    case 2:
      cout << "Alturas \n";
      cout << "------- \n";

      for (int b = 0; b < maxJugadores; b++) {
        cout << jugador[b].altura << endl;
      }
      
      cout << "\n";
    break;
    case 3:
      cout << "Edades \n";
      cout << "------ \n";

      for (int c = 0; c < maxJugadores; c++) {
        cout << jugador[c].edad << endl;
      }
      
      cout << "\n";
    break;
    case 4:
    break;
    default:
      cout << nom << " debes digitar una opción correspondiente \n";
      
      cout << "\n";
    }
  } while (opcion != 4);
} 