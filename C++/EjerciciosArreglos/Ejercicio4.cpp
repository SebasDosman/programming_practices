#include <iostream>
#include <math.h>
#include <iomanip>
#include <string>

using namespace std;

int main() {
  const int tamResist = 5;
  int resistencia[tamResist] = {16, 27, 39, 56, 81};
  const int tamCorriente = 5;
  int corriente[tamCorriente];
  const int tamPotencia = 5;
  int potencia[tamPotencia];
  double calculoPotencia = 0;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";
 
  for(int i = 0; i < sizeof(corriente) / sizeof(corriente[tamCorriente]); i++){
    cout << nom << " ingrese la corriente número " << i + 1 << endl;
    cin >> corriente[i];
    cout << "\n";
  }

  for (int j = 0; j < sizeof(potencia) / sizeof(potencia[tamPotencia]); j++){
    calculoPotencia = (resistencia[j] * (pow(corriente[j], 2)));
    potencia[j] = calculoPotencia;
  }

  cout << "Resistencia" << setw(15) << "Corriente" << setw(15) << "Potencia" << endl;
  cout << "------------------------------------------" << endl;

  for(int z = 0; z < sizeof(potencia) / sizeof(potencia[tamPotencia]); z++){
    cout << setw(6) << resistencia[z] << setw(16)<< corriente[z] << setw(16) << potencia[z] << endl;
  }
}