#include <iostream>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

int main() {
  string alumno, cadenaVacia;
  double notaFinal, np, npro, nt;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  do {
    cout << "Introduce el nombre del alumno \n";
    cin >> alumno;
    cout << "\n";

    cout << "Introduce la nota practica \n";
    cin >> np;;
    cout << "\n";

    cout << "Introduce la nota de problemas \n";
    cin >> npro;
    cout << "\n";

    cout << "Introduce la nota de teoria \n";
    cin >> nt;;
    cout << "\n";

    if ((np <= 10 && np >= 0) && (npro <= 10 && npro >= 0) && (nt <= 10 && nt >= 0)) {
      cout << "Alumno: " << alumno << "\n";
      cout << "Nota practica: " << np << "\n";
      cout << "Nota de problemas: " << npro << "\n";
      cout << "Nota de teoria: " << nt << "\n";
      cout << "\n";

      np *= 0.1;
      npro *= 0.5;
      nt *= 0.4;

      notaFinal = (np+npro+nt);

      cout << "La nota final es " << notaFinal << "\n";
      cout << "\n";
    } else {
      cout << "Has escrito una nota incorrecta, vuelve a intentarlo \n";
    }
  } while (!alumno.empty());
}