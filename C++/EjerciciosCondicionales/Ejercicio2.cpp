#include <iostream>
#include <string> 

using namespace std;

int main() {
  int temp;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;

  cout << nom << " digite la temperatura \n";
  cin >> temp;

  if (temp > 100) {
    cout << nom << " la temperatura está arriba del punto de ebullición del agua \n";
  } else {
    cout << nom << " la temperatura está abajo del punto de ebullición del agua \n";
  }
}