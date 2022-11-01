#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int galon = 10;
  double litro;

  while (galon <= 20) {
    litro = (galon * 3.785);

    cout << galon << setw(10) << litro << endl;

    galon++;
  }
}