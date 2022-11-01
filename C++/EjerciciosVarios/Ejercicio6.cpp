#include <iostream>
#include <string>

using namespace std;

int main() {
  int num1, num2, num3;
  double prom;
  string nom;

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite el primer número \n";
  cin >> num1;
  cout << nom << " digite el segundo número \n";
  cin >> num2;
  cout << nom << " digite el tercerr número \n";
  cin >> num3;
  cout << "\n";

  if (num1 > num2 && num1 > num3) {
    if (num2 > num3) {
      cout << "Número " << num1 << endl;
      cout << "Número " << num2 << endl;
      cout << "Número " << num3 << endl;
    } else {
      if (num3 > num2) {
        cout << "Número " << num1 << endl;
        cout << "Número " << num3 << endl;
        cout << "Número " << num2 << endl;
      }
    }
  } else {
    if (num2 > num1 && num2 > num3) {
      if (num1 > num3) {
        cout << "Número " << num2 << endl;
        cout << "Número " << num1 << endl;
        cout << "Número " << num3 << endl;
      } else {
        if (num3 > num1) {
          cout << "Número " << num2 << endl;
          cout << "Número " << num3 << endl;
          cout << "Número " << num1 << endl;
        }  
      }
    } else {
      if (num3 > num2 && num3 > num1) {
        if (num1 > num2) {
          cout << "Número " << num3 << endl;
          cout << "Número " << num1 << endl;
          cout << "Número " << num2 << endl;
        } else {
          if (num2 > num1) {
            cout << "Número " << num3 << endl;
            cout << "Número " << num2 << endl;
            cout << "Número " << num1 << endl;
          }
        }
      }
    }
  }
}