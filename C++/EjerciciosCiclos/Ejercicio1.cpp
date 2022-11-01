#include <iostream>
#include <string>

using namespace std;

int main() {
  int nummax, num, acu = 0;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el número hasta el que desea contar \n";
  cin >> nummax;
  cout << "\n";
  
  for (num = 1; num <= nummax; num++) {
    if (num % 2 != 0) {
      cout << "Número impar: " << num << "\n";
      acu += num;
    }
  } 
  
  cout << "\n";

  cout << nom << " la suma de los números impares hasta " << nummax << " es " << acu;
}