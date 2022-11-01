#include <iostream>
#include <string>

using namespace std;

int main() {
  int num = 1, acu = 0;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  while (num != 0) {
    cout << nom << " digite el número \n";
    cin >> num;

    cout << "\n";
    
    acu += num;
  }

  cout << nom << " la suma de los números es " << acu;
}