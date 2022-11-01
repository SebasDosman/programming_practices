#include <iostream>
#include <string>

using namespace std;

int main() {
  int suma = 0, num;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";
      
  cout << nom << " digite un numero \n";
  cin >> num;
  cout << "\n";

  for (int i = 1; i < num; i++) {  
    if (num % i == 0) {
      suma = suma + i;   
    }
  }

  if (suma == num) {                          
    cout << nom << " el numero es perfecto \n";
  } else {
    cout << nom << " el numero no es perfecto \n";
  }
}