#include <iostream>
#include <string>

using namespace std;

int main() {
  int num, sumneg, sumpos;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite un número \n";
  cin >> num;

  if (num > 0) {
    sumpos += num;
    cout << "Número positivo: " << sumpos << "\n";
  } else {
    sumneg += num;
    cout << "Número negativo: " <<sumneg << "\n";
  }
}
