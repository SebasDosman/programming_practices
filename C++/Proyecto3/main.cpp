#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
  
using namespace std;

void menu();
void creacionUsuario(struct usuarios, int);
void comprarTiquetes(struct usuarios, int);
int calculoTarifaPlena(string, int);

struct usuarios {
  string nombre;
  string apellido;
  string sexo;
  string cedula;
  string direccion;
  string telefono;
  string usuario;
  string contrasena;
  string tarjetaVip;
  long saldoTarjeta;
};

void menu() {
  cout << "--------------------------------------------------------------- \n";
  cout << "|                --------------------------                   | \n";
  cout << "|                ||  Bienvenido a RENFE  ||                   | \n";
  cout << "|                --------------------------                   | \n";
  cout << "|                                                             | \n";
  cout << "|           Escoja una de las siguientes opciones:            | \n";
  cout << "|                   1. Crear usuario VIP                      | \n";
  cout << "|                   2. Comprar tiquetes                       | \n";
  cout << "|                         3. Salir                            | \n";
  cout << "--------------------------------------------------------------- \n";
}

void creacionUsuario(struct usuarios usuario[], int cant) {
  for (int i = 0; i < cant; i++) {
    cout << "Digite su nombre \n";
    cin >> usuario[i].nombre;
    cout << "\n";

    cout << "Digite su apellido \n";
    cin >> usuario[i].apellido;
    cout << "\n";

    cout << "Digite su sexo \n";
    cin >> usuario[i].sexo;
    cout << "\n";

    cout << "Digite su cédula \n";
    cin >> usuario[i].cedula;
    cout << "\n";

    cout << "Digite su dirección de residencia \n";
    cin >> usuario[i].direccion;
    cout << "\n";

    cout << "Digite su teléfono \n";
    cin >> usuario[i].telefono;
    cout << "\n";

    cout << "Digite el usuario a crear \n";
    cin >> usuario[i].usuario;
    cout << "\n";

    cout << "Digite la contraseña \n";
    cin >> usuario[i].contrasena;
    cout << "\n";

    cout << "Digite su número de tarjeta VIP \n";
    cin >> usuario[i].tarjetaVip;
    cout << "\n";

    cout << "Digite el saldo de su tarjeta VIP \n";
    cin >> usuario[i].saldoTarjeta;
    cout << "\n";
  }
}

void comprarTiquetes(struct usuarios usuario[], int cant) {
  string ciudad, user, contrasena;
  int cantTiquetes, fila, columna, opcion, pago, cont, pagoVip, recargo, saldoTotal;
  const int filaMatriz = 10;
  const int columnaMatriz = 5;
  string asientos[filaMatriz][columnaMatriz];

  cout << "¡Bienvenido a la compra de tiquetes! \n";
  cout << "\n";

  cout << "Precios Tiquetes: \n"
  << "Cali: $50.000 \n"
  << "Bogota: $60.000 \n"
  << "Medellin: $85.000 \n"
  << "Cartagena: $120.000 \n";
  cout << "\n";

  cout << "Digite la ciudad (Primera letra en mayúscula y sin tildes) \n";
  cin >> ciudad;
  cout << "\n";

  cout << "Digite la cantidad de tiquetes que desea comprar de esa ciudad \n";
  cin >> cantTiquetes;
  cout << "\n";

  cout << setw(10) << "Puestos disponibles: \n";

  cout << "\n";

  for (int i = 0; i < filaMatriz; i++) {
    asientos[i][0] = "A";
    asientos[i][1] = "A";
    asientos[i][2] = "P";
    asientos[i][3] = "A";
    asientos[i][4] = "A";
  }

  cout << " ";

  for (int i = 0; i < columnaMatriz; i++) {
    cout << setw(5) << i << setw(5);
  }

  cout << "\n";

  for (int j = 0; j < filaMatriz; j++) {
    cout << j << setw(5);
    for (int y = 0; y < columnaMatriz; y++) {
      cout << asientos[j][y] << setw(5);
    }
    cout << "\n";
  }

  cout << "\n";

  for (int i = 0; i < cantTiquetes; i++) {
    do {
      cout << "Digite la fila del asiento a ocupar del tiquete número " << i + 1 << "\n";
      cin >> fila;
      cout << "\n";

      cout << "Digite la columna del asiento a ocupar del tiquete número " << i + 1 << "\n";
      cin >> columna;
      cout << "\n";

      if (asientos[fila][columna] == asientos[fila][2] || asientos[fila][columna].compare("X") == 0) {
        cout << "Debe escoger un asiento disponible \n";
        cout << "\n";
      }
    } while (asientos[fila][columna] == asientos[fila][2] || asientos[fila][columna].compare("X") == 0);

    asientos[fila][columna] = "X";
  }

  cout << " ";

  for (int i = 0; i < columnaMatriz; i++) {
    cout << setw(5) << i << setw(5);
  }

  cout << "\n";

  for (int j = 0; j < filaMatriz; j++) {
    cout << j << setw(5);
    for (int y = 0; y < columnaMatriz; y++) {
      cout << asientos[j][y] << setw(5);
    }
    cout << "\n";
  }

  cout << "\n";

  pago = calculoTarifaPlena(ciudad, cantTiquetes);

  do {
    cout << "Digite su opción de compra: \n"
    << "1. Compra Normal \n"
    << "2. Compra Cliente VIP \n"
    << "3. Salir \n";
    cin >> opcion;
    cout << "\n";

    ofstream archivoEntrada;
    ofstream archivoEntrada2;

    archivoEntrada.open("Factura.txt");
    archivoEntrada2.open("DatosCliente.txt");

    if (archivoEntrada.fail()) {
      cout << "No fue posible abrir el archivo de lectura \n";
    
      exit(1);
    }

    if (archivoEntrada2.fail()) {
      cout << "No fue posible abrir el archivo de lectura \n";
    
      exit(1);
    }

    if (opcion == 1) {
      cout << "¡Bienvenido a compra normal! \n";
      cout << "\n";

      cout << "Pago Tarifa Plena: $" << pago << endl;
      cout << "\n";

      cout << "Tiquetes Digitales \n";
      cout << "------------------ \n";
      cout << "Ciudad: " << ciudad << endl;
      cout << "Tiquetes: " << cantTiquetes << endl;

      for (int i = 0; i < filaMatriz; i++) {
        for (int j = 0; j < columnaMatriz; j++) {
          if (asientos[i][j] == "X") {
            cout << "Ubicación: " << i << ", " << j << endl;
          }
        }
      }

      cout << "\n";

      archivoEntrada << "Factura" << endl;
      archivoEntrada << "------------------" << endl;
      archivoEntrada << "Ciudad: " << ciudad << endl; 
      archivoEntrada << "Cantidad Tiquetes: " << cantTiquetes << endl;
      archivoEntrada << "Pago: " << pago << endl;

      archivoEntrada.close();
    } else {
      if (opcion == 2) {
        cout << "¡Bienvenido a compra de cliente VIP! \n";
        cout << "\n";

        cout << "Digite su usuario \n";
        cin >> user;
        cout << "\n";

        cout << "Digite su contraseña \n";
        cin >> contrasena;
        cout << "\n";

        for (int i = 0; i < cant; i ++) {
          if (usuario[i].usuario.compare(user) == 0 && usuario[i].contrasena.compare(contrasena) == 0) {
            cout << "Has ingresado correctamente \n";
            cout << "\n";

            pagoVip = (pago - (pago * 0.15));

            if (usuario[i].saldoTarjeta < pagoVip) {
              cout << "Debes recargar tu tarjeta Vip \n";
              cout << "\n";

              cout << "Digite la cantidad de saldo a recargar \n";
              cin >> recargo;
              cout << "\n";

              saldoTotal = usuario[i].saldoTarjeta + recargo;

              usuario[i].saldoTarjeta = saldoTotal;

              cout << "Datos Cliente VIP \n";
              cout << "Nombre: " << usuario[i].nombre << endl;
              cout << "Apellido: " << usuario[i].apellido << endl;
              cout << "Sexo: " << usuario[i].sexo << endl;
              cout << "Cédula: " << usuario[i].cedula << endl;
              cout << "Dirección: " << usuario[i].direccion << endl;
              cout << "Teléfono: " << usuario[i].telefono << endl;
              cout << "Usuario: " << usuario[i].usuario << endl;
              cout << "Contraseña: " << usuario[i].contrasena << endl;
              cout << "No. Tarjeta Vip: " << usuario[i].tarjetaVip << endl;
              cout << "Recargo: " << recargo << endl;
              cout << "Saldo: " << saldoTotal << endl;

              cout << "\n";

              archivoEntrada2 << "Factura" << endl;
              archivoEntrada2 << "Nombre: " << usuario[i].nombre << endl;
              archivoEntrada2 << "Apellido: " << usuario[i].apellido << endl;
              archivoEntrada2 << "Sexo: " << usuario[i].sexo << endl;
              archivoEntrada2 << "Cédula: " << usuario[i].cedula << endl;
              archivoEntrada2 << "Dirección: " << usuario[i].direccion << endl;
              archivoEntrada2 << "Teléfono: " << usuario[i].telefono << endl;
              archivoEntrada2 << "Usuario: " << usuario[i].usuario << endl;
              archivoEntrada2 << "Contraseña: " << usuario[i].contrasena << endl;
              archivoEntrada2 << "No. Tarjeta Vip: " << usuario[i].tarjetaVip << endl;
              archivoEntrada2 << "Recargo: " << recargo << endl;
              archivoEntrada2 << "Saldo: " << saldoTotal << endl;
            } else {
              cout << "Pago Tarifa VIP: $" << pagoVip << endl;
              cout << "\n";

              cout << "Tiquetes Digitales \n";
              cout << "------------------ \n";
              cout << "Ciudad: " << ciudad << endl;
              cout << "Tiquetes: " << cantTiquetes << endl;

              for (int i = 0; i < filaMatriz; i++) {
                for (int j = 0; j < columnaMatriz; j++) {
                  if (asientos[i][j] == "X") {
                    cout << "Ubicación: " << i << ", " << j << endl;
                  }
                }
              }

              cout << "\n";

              archivoEntrada << "Factura" << endl;
              archivoEntrada << "------------------" << endl;
              archivoEntrada << "Ciudad: " << ciudad << endl; 
              archivoEntrada << "Cantidad Tiquetes: " << cantTiquetes << endl;
              archivoEntrada << "Pago: " << pago << endl;
            }
          } else {
            cout << "No eres cliente Vip \n";
            cout << "\n";

            cout << "Debes pagar la tarifa normal \n";
            cout << "Pago Tarifa Plena: $" << pago << endl;
          }
        }

        cout << "\n";

      } else {
        if (opcion == 3) {
          cout << "¡Vuelva pronto!";
          break;
        } else {
          cout << "Debes digitar una opción correspondiente \n";
          cout << "\n";
        }
      }
    }
  } while (opcion != 3);
}

int calculoTarifaPlena(string ciudad, int cantTiquetes) {
  int pagoCiudad;

  if (ciudad.compare("Cali") == 0) {
    pagoCiudad = (50000 * cantTiquetes);
  } else {
    if (ciudad.compare("Bogota") == 0) {
      pagoCiudad = (60000 * cantTiquetes);
    } else {
      if (ciudad.compare("Medellin") == 0) {
        pagoCiudad = (85000 * cantTiquetes);
      } else {
        if (ciudad.compare("Cartagena") == 0) {
          pagoCiudad = (120000 * cantTiquetes);
        }
      }
    }
  }

  return pagoCiudad;
}

int main() {
  int opcion, cant;

  cout << "Autores: Juan Sebastián Dosman \n"
  << "Camilo Andrés Román \n";
  cout << "\n";

  menu();

  do {
    cin >> opcion;

    cout << "\n";

    if (opcion == 3) {
      cout << "¡Vuelva Pronto! \n";
      break;
    }

    cout << "Digite la cantidad de usuarios a crear \n";
    cin >> cant;
    cout << "\n";

    usuarios usuario[cant];

    creacionUsuario(usuario, cant);

    if (opcion == 1) {
      cout << "¡Bienvenido a la creación de usuario! \n";
      cout << "\n";

      cout << "El usuario ya ha sido creado con éxito \n";
      cout << "\n";

      cout << "El siguiente paso es comprar tus tiquetes \n";
      cout << "\n";

      comprarTiquetes(usuario, cant);
    } else {
      if (opcion == 2) {
        comprarTiquetes(usuario, cant);
        break;
      } else {
        if (opcion == 3) {
          cout << "¡Vuelva Pronto! \n";
          break;
        } else {
          cout << "Debes digitar una opción correspondiente \n";
          cout << "\n";
        }
      }
    }
  } while (opcion != 3);
}