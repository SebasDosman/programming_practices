#include <iostream>
#include <string>

using namespace std;

int main() {
  int edad, num, año18 = 0, alt175 = 0, acuedad = 0, acualtura = 0, mediaedad;
  double altura, mediaaltura;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite la cantidad de alumnos a registrar \n";
  cin >> num;
  cout << "\n";

  for (int i = 1; i <= num; i++) {
    cout << "Digite la edad del alumno " << i << "\n";
    cin >> edad;
    cout << "\n";

    if (edad > 18) {
      año18++;
    }

    acuedad += edad;

    cout << "Digite la altura del alumno " << i << "\n";
    cin >> altura;
    cout << "\n";

    if (altura > 1.75) {
      alt175++;
    }

    acualtura += altura;
  }

  mediaedad = (acuedad / num);
  mediaaltura = (acualtura / num);

  cout << "La edad media corresponde a " << mediaedad << "\n";
  cout << "La altura media corresponde a " << mediaaltura << "\n";
  cout << "La cantidad de alumnos mayores que 18 corresponde a " << año18 << " y la cantidad de alumnos con una estatura mayor a 1.75 corresponde a " << alt175 << "\n";
}