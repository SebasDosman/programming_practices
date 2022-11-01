#include <iostream>
#include <string>

using namespace std;

int main() {
  const int max = 1000;
  int num = 1, resp;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";
  
  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  do {
    cout << num << "\t";

    if (num % 20 == 0 && num != max) {
      cout << "\n";
      cout << "\n" << nom << ", ¿Desea continuar? \n" 
      << "1. Si \n"
      << "2. No \n";
      cin >> resp;
      cout << "\n";
    }
  } while (resp != 2 && num++ < max);
}