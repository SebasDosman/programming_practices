#define cantDatos 4

#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

void lecturaArchivo(string);
void escrituraArchivo(string);

int main() {
  string nombreArchivo, nom; 

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el nombre del archivo a trabajar \n";
  cin >> nombreArchivo;
  cout << "\n";

  lecturaArchivo(nombreArchivo);
  escrituraArchivo(nombreArchivo);
} 

void lecturaArchivo(string nombreArchivo) {
  string numParte;
  int cantInicial, cantVendida, cantMinima;

  ofstream archivoEntrada;
  ofstream archivoEntrada2;

  archivoEntrada.open(nombreArchivo);
  archivoEntrada2.open("Salida.txt");

  if (archivoEntrada.fail()) {
    cout << "No fue posible abrir el archivo de lectura \n";
    
    exit(1);
  }

  if (archivoEntrada2.fail()) {
    cout << "No fue posible abrir el archivo de lectura de salida \n";

    exit(1);
  }

  for (int i = 0; i < cantDatos; i++) {
    cout << "Digite el número de parte " << i + 1 << "\n";
    cin >> numParte;
    cout << "\n";

    cout << "Digite la cantidad inicial " << i + 1 << "\n";
    cin >> cantInicial;
    cout << "\n";

    cout << "Digite la cantidad vendida " << i + 1 << "\n";
    cin >> cantVendida;
    cout << "\n";

    cout << "Digite la cantidad mínima " << i + 1 << "\n";
    cin >> cantMinima;
    cout << "\n";

    archivoEntrada << numParte << "\t" << cantInicial << "\t" << cantVendida << "\t" << cantMinima << "\n";

    archivoEntrada2 << numParte << "\t" << cantVendida << "\t" << cantMinima << "\n";
  }

  archivoEntrada.close();
  archivoEntrada2.close();
} 

void escrituraArchivo(string nombreArchivo) {
  string numParte;
  int cantInicial, cantVendida, cantMinima;

  ifstream archivoSalida;
  ifstream archivoSalida2;

  archivoSalida.open(nombreArchivo);
  archivoSalida2.open("Salida.txt");

  if (archivoSalida.fail()) {
    cout << "No fue posible abrir el archivo de escritura \n";

    exit(1);
  }

  if (archivoSalida2.fail()) {
    cout << "No fue posible abrir el archivo de escritura de salida \n";

    exit(1);
  }

  cout << "Número Parte \t" << "Cant. Inicial \t"  << "Cant. Vendida \t" << "Cant. Mínima \t" << "\n";
  cout << "------------------------------------------------------------";
  cout << "\n";

  archivoSalida >> numParte >> cantInicial >> cantVendida >> cantMinima;

  while (archivoSalida.good()) {
    cout << setw(8) << numParte << setw(15) << cantInicial << setw(16) << cantVendida << setw(16) << cantMinima << endl;

    archivoSalida >> numParte >> cantInicial >> cantVendida >> cantMinima;
  } 

  cout << "\n";

  cout << "Número Parte \t" << "Balance Actual \t" << "Cant. Mínima \t" << "\n";
  cout << "--------------------------------------------";
  cout << "\n";

  archivoSalida2 >> numParte >> cantVendida >> cantMinima;

  while (archivoSalida2.good()) {
    cout << setw(8) << numParte << setw(16) << cantVendida << setw(15) << cantMinima << endl;

    archivoSalida2 >> numParte >> cantVendida >> cantMinima;
  }

  archivoSalida.close();
  archivoSalida2.close();
}