#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int num = 2;
  
  while (num <= 10) {
    cout << num << setw(4);

    num += 2;
  }
}