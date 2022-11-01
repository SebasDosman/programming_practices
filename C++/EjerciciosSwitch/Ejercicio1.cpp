#include <iostream>
#include <string>

using namespace std;

int main() {
  char let_calif;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite la calificación \n";
  cin >> let_calif;

  switch (let_calif) {
    case 'A':
      cout << "La calificación numérica está entre 90 y 100\n";
    break;
    case 'B':
      cout << "La calificación numérica está entre 80 y 89.9\n";
    break;
    case 'C':
      cout << "La calificación numérica está entre 70 y 79.9\n";
    break;
    case 'D':
      cout << "Como va a explicar esta\n";
    break;
    default:
      cout << "Por supuesto que no tuve nada que ver con mi  calificación.\n";    
      cout << "Debe ser culpa del profesor \n";
  }
}