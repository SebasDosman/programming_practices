#define cantDatos 4

#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

void lecturaArchivo(string);
void escrituraArchivo(string);
int calculoPagoRegular(int, double);
int calculoPagoExtra(int, double);
int calculoPagoBruto(int, int);

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
  string nombre;
  double tarifa, pagoRegular, pagoExtra, pagoBruto;
  int horas;

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
    cout << "Digite el nombre " << i + 1 << "\n";
    cin >> nombre;
    cout << "\n";

    cout << "Digite la tarifa número " << i + 1 << "\n";
    cin >> tarifa;
    cout << "\n";

    cout << "Digite las horas del trabajador " << i + 1 << "\n";
    cin >> horas;
    cout << "\n";

    archivoEntrada << nombre << "\t" << tarifa << "\t" << horas << "\n";

    pagoRegular = calculoPagoRegular(horas, tarifa);
    pagoExtra = calculoPagoExtra(horas, tarifa);
    pagoBruto = calculoPagoBruto(pagoRegular, pagoExtra);

    archivoEntrada2 << nombre << "\t" << tarifa << "\t" << pagoRegular << "\t" << pagoExtra << "\t" << pagoBruto << "\n";
  }

  archivoEntrada.close();
  archivoEntrada2.close();
}

void escrituraArchivo(string nombreArchivo){
  string nombre;
  double tarifa, pagoRegular, pagoExtra, pagoBruto;
  int horas;

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

  cout << "\n";

  cout << setw(10) << "Nombre " << setw(14) <<  "Tarifa " << setw(9) <<  "Horas" << "\n";
  cout << "------------------------------------";
  cout << "\n";

  archivoSalida >> nombre >> tarifa >> horas;

  while (archivoSalida.good()) {
    cout << setw(12) << nombre << setw(10) << tarifa << setw(9) << horas << endl;

    archivoSalida >> nombre >> tarifa >> horas;
  }

  cout << "\n";

  cout << setw(11) << "Nombre " << setw(13) <<  "Tarifa " << setw(17) <<  "Pago Regular " << setw(12) << "Pago Extra" << setw(15) << "Pago Bruto " << "\n";
  cout << "-----------------------------------------------------------------------";
  cout << "\n";

  archivoSalida2 >> nombre >> tarifa >> pagoRegular >> pagoExtra >> pagoBruto;

  while (archivoSalida2.good()) {
    cout << setw(12) << nombre << setw(10) << tarifa << setw(13) << pagoRegular << setw(15) << pagoExtra << setw(15) << pagoBruto << endl;

    archivoSalida2 >> nombre >> tarifa >> pagoRegular >> pagoExtra >> pagoBruto;
  }

  archivoSalida.close();
  archivoSalida2.close();
}

int calculoPagoRegular(int horas, double tarifa) {
  double pagoRegular = 0;

  if (horas <= 40) {
    pagoRegular = (horas * tarifa);
  } else {
    if (horas > 40) {
      pagoRegular = (40 * tarifa);
    }
  }

  return pagoRegular;
}

int calculoPagoExtra(int horas, double tarifa) {
  double pagoExtra = 0;
 
  if (horas > 40) {
    pagoExtra = (horas - 40) * (tarifa * 1.5);
  }

  return pagoExtra;
}

int calculoPagoBruto(int pagoRegular, int pagoExtra) {
  double pagoBruto;

  pagoBruto = (pagoRegular + pagoExtra);

  return pagoBruto;
}