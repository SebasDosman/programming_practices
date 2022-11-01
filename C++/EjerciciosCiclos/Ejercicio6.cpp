#include <iostream>
#include <string>

using namespace std;

int main() {
  int precio = 0, acu = 0, acutotal = 0, iva = 0, monto;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  do {
    cout << nom << " digite el precio del artículo \n";
    cin >> precio;
    cout << "\n";

    acu += precio;
  } while (precio != -1);
  
  acutotal = (acu + 1);
  iva = (acutotal * 0.15);
  monto = (acutotal + iva);

  if (acutotal != 0) {
    cout << nom << " la suma del precio de todos los artículos corresponde a $" << acutotal << " y el cálculo del IVA corresponde a $" << iva << "\n";
    cout << "Monto total a pagar: $" << monto;
  } else {
    cout << nom << " no digitaste ningún artículo";
  }
}