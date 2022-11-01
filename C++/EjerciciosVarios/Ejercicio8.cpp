#include <iostream>
#include <string>

using namespace std;

int main() {
  string nom;
  int x, y;
  
  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el valor de x \n";
  cin >> x;
  cout << nom << " digite el valor de y \n";
  cin >> y;
  cout << "\n";

  if((3 * x) - y == 4){
    cout << nom << " los valores " << x << ", " << y << " pertenecen a la función y = 3x -4"; 
  } else {
    cout << nom << " los valores " << x << ", " << y << " no pertenecen a la función y = 3x -4";
  }
}