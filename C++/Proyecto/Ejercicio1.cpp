#include <iostream>
#include <string>

using namespace std;

int main() {
  string nom;
  int monto, opcion, cantbilletes;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el monto a retirar \n";
  cin >> monto;
  cout << "\n";

  if (monto % 10000 == 0 && monto <= 700000) {
    cout << nom << " escoja la opción de billetes a retirar \n"
    << "1. $10.000 \n"
    << "2. $20.000 \n"
    << "3. $50.000 \n"
    << "4. $100.000 \n";
    cin >> opcion;
    cout << "\n";

    switch (opcion) {
      case 1:
        if (monto >= 10000) {
          cantbilletes = (monto / 10000);

          cout << "Monto a retirar: " << monto << "\n";
          cout << "Denominación escogida: $10.000 \n";
          cout << "Cantidad de billetes: " << cantbilletes;
        } else {
          cout << nom << " el monto a retirar debe ser mayor o igual a $10.000";
        }
      break;
      case 2:
        if (monto >= 20000) {
          cantbilletes = (monto / 20000);

          cout << "Monto a retirar: " << monto << "\n";
          cout << "Denominación escogida: $20.000 \n";
          cout << "Cantidad de billetes: " << cantbilletes;
        } else {
          cout << nom << " el monto a retirar debe ser mayor o igual a $20.000";
        }
      break;
      case 3:
        if (monto >= 50000) {
          cantbilletes = (monto / 50000);

          cout << "Monto a retirar: " << monto << "\n";
          cout << "Denominación escogida: $50.000 \n";
          cout << "Cantidad de billetes: " << cantbilletes;
        } else {
          cout << nom << " el monto a retirar debe ser mayor o igual a $50.000";
        }
      break;
      case 4:
        if (monto >= 100000) {
          cantbilletes = (monto / 100000);

          cout << "Monto a retirar: " << monto << "\n";
          cout << "Denominación escogida: $100.000 \n";
          cout << "Cantidad de billetes: " << cantbilletes;
        } else {
          cout << nom << " el monto a retirar debe ser mayor o igual a $100.000";
        }
      break;
      default:
        cout << nom << " debes digitar una de las opciones disponibles";
      ;
    }
  } else {
    cout << nom << " no puedes retirar la cantidad de $" << monto;
  }
}