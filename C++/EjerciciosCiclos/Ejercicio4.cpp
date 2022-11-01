#include <iostream>
#include <string>

using namespace std;

int main() {
  int monto, interes, monto2, i = 0;
  string nom;
    
  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el monto a calcular \n";
  cin >> monto;
  cout << "\n";

  monto2 = (monto * 2);

  while (monto <= monto2) { 
    interes = (monto * 0.05);
    monto += interes;

    i++; 
  }

  cout << "Monto total: $" << monto << "\n";
  cout << "\n";

  cout << nom << " el monto tardará " << i << " años en duplicarse";
}