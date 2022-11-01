#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int pies = 3;
  double metros;

  while (pies <= 30) {
    metros = (pies / 3.281);

    cout << pies << setw(10) << metros << endl;

    pies += 3; 
  }
}