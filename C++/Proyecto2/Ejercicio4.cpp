#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
  string nom, nomPaciente, edad, diagnostico, prioridad;
  const int tamColum = 4;
  const int tamFilas2 = 3;
  const int tamColum2 = 2;
  int prioridades[tamFilas2][tamColum2], tamFilas, contBaja = 0 , contMedia = 0, contAlta = 0, porcentajeBaja, porcentajeMedia, porcentajeAlta;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";
 
  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite la cantidad de pacientes en urgencia \n";
  cin >> tamFilas;
  cout << "\n";

  string pacientes[tamFilas][tamColum];

  for (int i = 0; i < tamFilas; i++) {
    cout << nom << " digite el nombre del paciente número " << i + 1 << "\n";
    cin >> nomPaciente;
    cout << "\n";

    pacientes[i][0] = nomPaciente;

    cout << nom << " digite la edad del paciente número " << i + 1 << "\n";
    cin >> edad;
    cout << "\n";

    pacientes[i][1] = edad;

    cout << nom << " digite el diagnóstico del paciente número " << i + 1 << "\n";
    cin >> diagnostico;
    cout << "\n";

    pacientes[i][2] = diagnostico;

    cout << nom << " digite la prioridad del paciente número " << i + 1 << "\n";
    cin >> prioridad;
    cout << "\n";

    pacientes[i][3] = prioridad;

    if (pacientes[i][3] == "Baja") {
        contBaja++;
      } else {
        if (pacientes[i][3] == "Media") {
          contMedia++;
        } else {
          if (pacientes[i][3] == "Alta") {
            contAlta++;
          }
        }
      }
  }

  prioridades[0][0] = contBaja;
  prioridades[1][0] = contMedia;
  prioridades[2][0] = contAlta;

  porcentajeBaja = (100 / tamFilas) * contBaja;
  prioridades[0][1] = porcentajeBaja;
  porcentajeMedia = (100 / tamFilas) * contMedia;
  prioridades[1][1] = porcentajeMedia;
  porcentajeAlta = (100 / tamFilas) * contAlta;
  prioridades[2][1] = porcentajeAlta;

  cout << "Nombre" << setw(8) << "Edad" << setw(15) << "Diagnóstico" << setw(12) << "Prioridad" << "\n";
  cout << "-----------------------------------------";
  cout << "\n";

  for (int a = 0; a < tamFilas; a++) {
    for (int b = 0; b < tamColum; b++) {
      cout << pacientes[a][b] << "\t" << "\t";
    }
    cout << "\n";
  }
  
  cout << "\n";

  cout << "Prioridad \t" << "Cantidad \t" << "Porcentaje" << "\n";
  cout << "----------------------------------";
  cout << "\n";

  cout << setw(5) << "Baja" << setw(12) << prioridades[0][0] << setw(12) << prioridades[0][1] << "% \n";
  cout << setw(5) << "Media" << setw(12) << prioridades[1][0] << setw(12) << prioridades[1][1] << "% \n";
  cout << setw(5) << "Alta" << setw(12) << prioridades[2][0] << setw(12) << prioridades[2][1] << "% \n";
}