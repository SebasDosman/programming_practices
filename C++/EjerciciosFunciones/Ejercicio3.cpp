#include <iostream>
#include <string>
#include <math.h>
#include <iomanip>

using namespace std;

void calculoNum(int);

int main() {
  string nom;
  int num;

  cout << "Autor: Juan Sebastián Dosman \n";
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el número \n";
  cin >> num;
  cout << "\n";

  calculoNum(num);
}

void calculoNum(int num) {
  int result;

  cout << "Tablas De Multilpicar \n";
  cout << "--------------------- \n";

  for (int i = 1; i <= 10; i++) {
    result = (num * i); 
    cout << setw(6) << num << " * " << i << " = " << result << "\n";
  }

  cout << "\n";

  cout << "Elevación Al Cuadrado \n";
  cout << "--------------------- \n";
  cout << setw(6) << num << " ^ 2 = " << pow(num, 2) << "\n";
  cout << "\n";

  cout << "Elevación Al Cubo \n";
  cout << "----------------- \n";
  cout << setw(4) << num << " ^ 3 = " << pow(num, 3) << "\n";
  cout << "\n";
}