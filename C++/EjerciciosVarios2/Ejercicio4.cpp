#include <iostream>

using namespace std;

int main() {
  int pl, cl, result, acu = 0, acuPrecio = 0, cant1;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (int cod = 1; cod <= 5; cod++) {
    cout << nom << " digite el precio por litro del artículo " << cod << "\n";
    cin >> pl;
    cout << "\n";

    cout << nom << " digite la cantidad de ventas en litro del artículo " << cod << "\n";
    cin >> cl;
    cout << "\n";

    if (cod == 1) {
      cant1 = cl;
    }

    result = (pl * cl);

    cout << "------------------------" << "\n";
    cout << "Código De Artículo: "<< cod << "\n";
    cout << "Precio Por Litro: " << pl << "\n";
    cout << "Ventas Por Litro: " << cl << "\n";
    cout << "Valor De Venta: " << result << "\n";
    cout << "------------------------" << "\n";

    if (result >= 600) {
      acu++;
    }

    acuPrecio += result;

    cout << "\n";
  }

  cout << "Facturación Total: " << acuPrecio << "\n";
  cout << "Cantidad Ventas Litros Artículo 1: " << cant1 << "\n";
  cout << "Facturas Por Encima De $600: " << acu << "\n";
  cout << "------------------------------" << "\n";  
}