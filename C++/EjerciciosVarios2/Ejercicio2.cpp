#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
  const int tamFilas = 2;
  const int tamColum = 3;
  string producto[tamFilas][tamColum];
  string nomProducto, cantProducto, precioProducto, nom, busqueda, cantidad2, precio2;
  int num, opcion;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  for (int i = 0; i < tamFilas; i++) {
    cout << nom << " digite el nombre del producto \n";
    cin >> nomProducto;
    cout << "\n";

    producto[i][0] = nomProducto;

    cout << nom << " digite la cantidad del producto \n";
    cin >> cantProducto;
    cout << "\n";

    producto[i][1] = cantProducto;

    cout << nom << " digite el precio del producto \n";
    cin >> precioProducto;
    cout << "\n";

    producto[i][2] = precioProducto;
  }

  do {
    cout << nom << " digite una de las siguientes opciones\n"
    << "1. Dar de alta un producto nuevo \n"
    << "2. Buscar un producto por su nombre \n"
    << "3. Modificar el stock y precio de un producto dado \n"
    << "4. Visualizar los datos en pantalla \n"
    << "5. Salir \n";
    cin >> num;
    cout << "\n";

    switch (num) {
      case 1:
        cout << nom << " digite el nombre del producto a dar de alta\n";
        cin >> busqueda;
        cout << "\n";

        for (int x = 0; x < tamFilas; x++) {
          for (int y = 0; y < tamColum; y++) {
            if (busqueda == producto[x][y]) {
              producto[x][0] = "";
              producto[x][1] = "";
              producto[x][2] = "";
            }
          }
        }
      break;
      case 2:
        cout << nom << " digite el nombre del producto \n";
        cin >> busqueda;
        cout << "\n";

        for (int a = 0; a < tamFilas; a++) {
          for (int b = 0; b < tamColum; b++) {
            if (busqueda == producto[a][b]) {
              cout << "Nombre Producto" << setw(12) << "Cantidad" << setw(12) << "Precio \n";
              cout << "-------------------------------------";
              cout << "\n";

              cout << setw(10) << producto[a][0] << setw(14) << producto[a][1] << setw(13) << producto[a][2];
              cout << "\n";
            break;
            }
          }
        }

        cout << "\n";
      break;
      case 3:
        cout << nom << " digite el nombre del producto a modificar \n";
        cin >> busqueda;
        cout << "\n";

        for (int m = 0; m < tamFilas; m++) {
          for (int l = 0; l < tamColum; l++) {
            if (busqueda == producto[m][l]) {
              cout << nom << " digite la cantidad nueva del producto seleccionado \n";
              cin >> cantidad2;
              cout << "\n";

              producto[m][1] = cantidad2;

              cout << nom << " digite el precio nuevo del producto seleccionado \n";
              cin >> precio2;
              cout << "\n";

              producto[m][2] = precio2;
            }
          }
        }
      break;
      case 4:
        cout << "Nombre Producto" << setw(12) << "Cantidad" << setw(12) << "Precio \n";
        cout << "-------------------------------------";
        cout << "\n";

        for (int z = 0; z < tamFilas; z++) {
          cout << setw(10) << producto[z][0] << setw(14) << producto[z][1] << setw(13) << producto[z][2];
          cout << "\n";
        }

        cout << "\n";
      break;
    }
  } while (num != 5);

  cout << nom << " gracias por usar el programa";
}