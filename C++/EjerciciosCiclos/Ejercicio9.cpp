#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int celsius = 10;
  double farenheit;

  while (celsius <= 60) {
    farenheit = (9.0 / 5.0) * celsius + 32;

    cout << celsius << setw(5) << farenheit << endl;

    celsius += 10;
  }
}