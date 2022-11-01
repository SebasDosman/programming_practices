#include <iostream>
#include <string> 

using namespace std;

double promedioNumeros(int num, int acu, int max);

int main() {
  int num, max, i, j = 1, pos = 0, neg = 0, prim = 0, residuo = 0,acupos = 0, acuneg = 0, acuprim = 0;
  double promprim = 0, prompos = 0, promneg = 0;
  string nom;
  
  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " digite la cantidad de números a leer \n";
  cin >> max;
  cout << "\n";

  for (i = 1; i <= max; i++) {
    cout << nom << " digite el número \n";
    cin >> num;
    cout << "\n";

    for (j = 1; j <= num; j++) {
      if (num % j == 0) {
        residuo++;
      }
    } 

    if (residuo == 2) {
      cout << num << " es un número primo \n";
      prim++;
      acuprim += num;
    }

    j = 1;
    residuo = 0;

    cout << "\n";

    if (num > 0) {
      cout << num << " es un número positivo \n";
      pos++;
      acupos += num;
      cout << "\n";
    } else {
      if (num < 0) {
        cout << num << " es un número negativo \n";
        neg++;
        acuneg += num;
        cout << "\n";
      }
    }
  }

  promprim = promedioNumeros (prim, acuprim, max);
  prompos = promedioNumeros (pos, acupos, max);
  promneg = promedioNumeros (neg, acuneg, max);

  cout << nom << " la cantidad de números leídos fue " << max << "\n";
  cout << nom << " la cantidad de números primos fue " << prim << " y su promedio fue " << promprim << "\n";
  cout << nom << " la cantidad de números positivos fue " << pos << " y su promedio fue " << prompos << "\n";
  cout << nom << " la cantidad de números negativos fue " << neg << " y su promedio fue " << promneg << "\n";
}

double promedioNumeros (int num, int acu, int max) {
  double prom;
  
  if (num > 1 && acu != 0 && max != 0) {
    prom = (acu / max);
  } else {
    if (num == 1) {
      prom = acu;
    } else {
      prom = 0;
    }
  }

  return prom;
}