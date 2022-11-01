#include <iostream>
#include <string>

using namespace std;

int main() {
  int num, aux, inverso = 0, cifra;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Dgite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " introduce el número a comprobar si es capicúa \n";
  cin >> num; 
  cout << "\n";                                          
       
  aux = num;

  while (aux != 0){
    cifra = (aux % 10);
    inverso = (inverso * 10 + cifra);
    aux = (aux / 10);
  }

  cout << "Número: " << num << "\n";
  cout << "Número inverso: " << inverso << "\n";
  cout << "\n";
    
  if (num == inverso) {
    cout << nom << " el número es capicúa";
  } else {
    cout << nom << " el número no es capicúa";
  }
}
