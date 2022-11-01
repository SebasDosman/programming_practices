#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include <cstdio>
#include <string>

using namespace std;

void lecturaArchivo(string, int);
void escrituraArchivo(string);
double calculoNomina(double, double);

int main() {
  string nombreArchivo, nom;
  int cantTrabajadores = 0;

  cout << "Autor: Juan Sebastián Dosman \n";
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el nombre del archivo a trabajar \n";
  cin >> nombreArchivo;
  cout << "\n";

  cout << nom << " digite la cantidad de trabajadores \n";
  cin >> cantTrabajadores;
  cout << "\n";

  lecturaArchivo(nombreArchivo, cantTrabajadores);
  escrituraArchivo(nombreArchivo);

  return 0;
} 

void lecturaArchivo(string nombreArchivo, int cantTrabajadores) {
  string nomTrabajador, numSeguro;
  double tarifaHoras, horasTrabajadas, nomina;

  ofstream archivoEntrada;
  ofstream archivoEntrada2;

  archivoEntrada.open(nombreArchivo.c_str());
  archivoEntrada2.open("Nomina.txt");

  if (archivoEntrada.fail()) {
    cout << "No fue posible abrir el archivo de escritura \n";

    exit(1);
  }

  if (archivoEntrada2.fail()) {
    cout << "No fue posible abrir el archivo de escritura de nomina \n";

    exit(1);
  }

  for (int i = 1; i <= cantTrabajadores; i++) {
    cout << "Digite el nombre del trabajador " << i << "\n";
    cin >> nomTrabajador;
    cout << "\n";

    cout << "Digite el número de seguro social del trabajador " << i << "\n";
    cin >> numSeguro;
    cout << "\n";

    cout << "Digite la tarifa en horas del trabajador " << i << "\n";
    cin >> tarifaHoras;
    cout << "\n";

    cout << "Digite las horas trabajadas por el trabajador " << i << "\n";
    cin >> horasTrabajadas;
    cout << "\n";

    nomina = calculoNomina(tarifaHoras, horasTrabajadas);

    archivoEntrada << nomTrabajador << "\t" << numSeguro << "\t" << tarifaHoras << "\t" << horasTrabajadas << "\t" << endl;

    archivoEntrada2 << numSeguro << "\t" << nomTrabajador << "\t" << nomina << endl;
  }

  archivoEntrada.close();
  archivoEntrada2.close();
}

void escrituraArchivo(string nombreArchivo) {
  string nomTrabajador, numSeguro;
  double tarifaHoras, horasTrabajadas, nomina;

  ifstream archivoSalida;
  ifstream archivoSalida2;

  archivoSalida.open(nombreArchivo);
  archivoSalida2.open("Nomina.txt");

  if (archivoSalida.fail()) {
    cout << "No fue posible abrir el archivo de lectura \n";

    exit(1);
  }

  if (archivoSalida2.fail()) {
    cout << "No fue posible abrir el archivo de lectura de la nomina \n";

    exit(1);
  }

  cout << "\t" << "Nombres \t" << "Número Seguro Social \t" << "Tarifa Hora \t" << "Horas trabajadas" << "\n";
  cout << "\t" <<"--------------------------------------------------------------------";
  cout << "\n";

  archivoSalida >> nomTrabajador >> numSeguro >> tarifaHoras >> horasTrabajadas;

  while (archivoSalida.good()) {
    cout << setw(10) << nomTrabajador << setw(17) << numSeguro << setw(21) << tarifaHoras << setw(17) << horasTrabajadas << endl;

    archivoSalida >> nomTrabajador >> numSeguro >> tarifaHoras >> horasTrabajadas;
  }

  cout << "\n";

  cout << "\t" << "Número Seguro Social \t" << "Nombres \t" << "Pago Bruto" << "\n";
  cout << "\t" <<"--------------------------------------------------";
  cout << "\n";

  archivoSalida2 >> numSeguro >> nomTrabajador >> nomina;

  while (archivoSalida2.good()) {
    cout << setw(15) << numSeguro << setw(20) << nomTrabajador << setw(12) << nomina << endl;

    archivoSalida2 >> numSeguro >> nomTrabajador >> nomina;
  }

  archivoSalida.close();
  archivoSalida2.close();
}

double calculoNomina(double tarifa, double horas) {
  double nomina;

  nomina = (tarifa * horas);

  return nomina;
}