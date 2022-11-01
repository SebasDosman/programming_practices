#include <iostream>
#include <string>

using namespace std;

int main() {
	int n, ancho;
  string nom; 

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

	cout << nom << " digite un numero entero impar \n";
	cin >> n;
  cout << "\n";

	ancho = (n / 2);

	for (int i = 0; i < n / 2 + 1; i++) {
		for (int j = 0; j < ancho - i; j++) {
			cout << " ";
		}
		for (int j = 0; j < 2 * i + 1; j++) {
			cout << "*";
		}
		cout << "\n";
	}

	for (int i = ancho - 1; i >= 0; i--) {
		for (int j = 0; j < ancho - i; j++) {
			cout << " ";
		}
		for (int j = 0; j < 2 * i + 1; j++) {
			cout << "*";
		}
		cout << "\n";
	}
}