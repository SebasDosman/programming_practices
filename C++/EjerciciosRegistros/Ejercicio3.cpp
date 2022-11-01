#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

struct equiposFutbol {
  string nombre;
  int victorias;
  int derrotas;
  int empates;
  int golesFavor;
  int golesContra;
  string nomGoleador;
  int golesGoleador;
};

struct equiposBaloncesto {
  string nombre;
  int victorias;
  int derrotas;
  int perdidasBalon;
  int rebotesCapturados;
  string anotadorTriples;
  int triplesAnotador; 
};

int main() {
  string nom;
  int numFutbol, numBaloncesto;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite la cantidad de equipos de futbol \n";
  cin >> numFutbol;
  cout << "\n";

  equiposFutbol equipoF[numFutbol]; 

  cout << nom << " digite la cantidad de equipos de baloncesto \n";
  cin >> numBaloncesto;
  cout << "\n";

  equiposBaloncesto equipoB[numBaloncesto];

  for (int i = 0; i < numFutbol; i++) {
    cout << nom << " digite el nombre del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].nombre;
    cout << "\n";

    cout << nom << " digite el número de victorias del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].victorias;
    cout << "\n";

    cout << nom << " digite el número de derrotas del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].derrotas;
    cout << "\n";

    cout << nom << " digite el número de empates del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].empates;
    cout << "\n";

    cout << nom << " digite el número de goles a favor del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].golesFavor;
    cout << "\n";

    cout << nom << " digite el número de goles en contra del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].golesContra;
    cout << "\n";

    cout << nom << " digite el nombre del goleador del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].nomGoleador;
    cout << "\n";

    cout << nom << " digite los goles del goleador del equipo de futbol " << i + 1 << endl;
    cin >> equipoF[i].golesGoleador;
    cout << "\n";
  }

  for (int a = 0; a < numBaloncesto; a++) {
    cout << nom << " digite el nombre del equipo de baloncesto " << a + 1 << endl;
    cin >> equipoB[a].nombre;
    cout << "\n";

    cout << nom << " digite el número de victorias del equipo de baloncesto " << a + 1 << endl;
    cin >> equipoB[a].victorias;
    cout << "\n";

    cout << nom << " digite el número de derrotas del equipo de baloncesto " << a + 1 << endl;
    cin >> equipoB[a].derrotas;
    cout << "\n";

    cout << nom << " digite el número de perdidas de balón del equipo de baloncesto " << a + 1 << endl;
    cin >> equipoB[a].perdidasBalon;
    cout << "\n";

    cout << nom << " digite el número de rebotes capturados del equipo de baloncesto " << a + 1 << endl;
    cin >> equipoB[a].rebotesCapturados;
    cout << "\n";

    cout << nom << " digite el nombre del mejor anotador de triples del equipo de baloncesto " << a + 1 << endl;
    cin >> equipoB[a].anotadorTriples;
    cout << "\n";

    cout << nom << " digite el número de triples del mejor triplista del equipo de futbol " << a + 1 << endl;
    cin >> equipoB[a].triplesAnotador;
    cout << "\n";
  }

  for (int b = 0; b < numFutbol; b++) {
    cout << "Nombre: " << equipoF[b].nombre << endl;
    cout << "Derrotas: " << equipoF[b].derrotas << endl;
    cout << "Victorias: " << equipoF[b].victorias << endl;
    cout << "Empates: " << equipoF[b].empates << endl;
    cout << "Goles Favor: " << equipoF[b].golesFavor << endl;
    cout << "Goles Contra: " << equipoF[b].golesContra << endl;
    cout << "Goleador: " << equipoF[b].nomGoleador << endl;
    cout << "Goles: " << equipoF[b].golesGoleador << endl;
  }

  cout << "\n";

  for (int c = 0; c < numBaloncesto; c++) {
    cout << "Nombre: " << equipoB[c].nombre << endl;
    cout << "Derrotas: " << equipoB[c].derrotas << endl;
    cout << "Victorias: " << equipoB[c].victorias << endl;
    cout << "Perdidas Balón: " << equipoB[c].perdidasBalon << endl;
    cout << "Rebotes Capturados: " << equipoB[c].rebotesCapturados << endl;
    cout << "Mejor Triplista: " << equipoB[c].anotadorTriples << endl;
    cout << "Triples: " << equipoB[c].triplesAnotador << endl;
  }

  cout << "\n";
} 