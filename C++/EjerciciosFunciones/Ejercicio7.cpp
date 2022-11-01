#include <iostream>
#include <string>

using namespace std;

int MCD(int, int);
int MCM(int, int);
void MCD2();

int main() {
  int cantNum;
  string nom;

  cout << "Autores: Juan Sebastián Dosman \n"
  cout << "\n";

  cout << "Digite su nombre \n";
  cin >> nom;
  cout << "\n";

  cout << nom << " ingrese la cantidad de números a calcular \n";
  cin >> cantNum;
  cout << "\n";

  if (cantNum == 2 || cantNum == 3) {
    if (cantNum == 2) {
      int num1, num2;

      cout << nom << " ingrese el primer número \n";
      cin >> num1;
      cout << "\n";

      cout << nom << " ingrese el segundo numero \n";
      cin >> num2; 
      cout << "\n";    
      
      cout << "El máximo común divisor es " << MCD(num1, num2) << endl;
      cout << "\n";

      cout << "El mínimo común múltiplo es " << MCM(num1, num2) << endl;
      cout << "\n";
    } else {
      MCD2(); 
    }
  } else {
    cout << nom << " solo puedes ingresar 2 0 3 números " << endl;
    cout << "\n";
  }
}

int MCD(int num1, int num2) {
  int residuo, divisor;

  do {
    residuo = (num1 % num2);

    if (residuo != 0) {
      num1 = num2;
      num2 = residuo;
    } else {
      divisor = num2;
    }
  } while (residuo != 0);

  return divisor;
}

void MCD2() {
  int numero, divisible, residuo, numeros[3];
  
  for (int i = 0; i < 3; i++) {
    do{
      cout << "Ingrese el número " << i + 1 << endl;
      cin>>numero;
      cout << "\n";

      numeros[i] = numero;
    } while (3 < 0);

    if (i == 0) {
      divisible = numero;
    } 

    do {
      residuo = (divisible % numero);
      divisible = numero;
      numero = residuo;
    } while (residuo != 0);
  }

  cout << "El máximo común divisor es " << divisible << endl;

  int valor, i, a = numeros[0], b = numeros[1], c = numeros[2], mayor, menor1, menor2;

  if (b >= a && b >= c) {
    mayor = b;
    menor1 = a;
    menor2 = c;
  } else {
    if (c >= b && c >= a) {
      mayor=c;
      menor1=b;
      menor2=a;
    } else {
      mayor=a;
      menor1=b;
      menor2=c;
    }

  if ((mayor % menor1) == 0 && (mayor % menor2) == 0) {
    cout << "El mínimo común múltiplo es " << mayor << endl;
  } else {
    if ((mayor % menor1) == 0 && (mayor % menor2) != 0) {
      for (i = 2; i <= menor2; i++) {
        valor = (mayor * i);

        if((valor % menor2) == 0){     
          cout << "El mínimo común múltiplo es " << valor << endl;
          break;
        }
      }
    } else {
      if ((mayor % menor1) != 0 && (mayor % menor2) == 0){
        for(i = 2; i <= menor1; i++) {
          valor = (mayor * i);

          if ((valor % menor1) == 0) {
            cout << "El minimo común múltiplo es " << valor << endl;
            break;
          }
        }
      } else {
        if ((mayor % menor1) != 0 && (mayor % menor2) != 0) {
          for (i = 2; i <= (menor1 * menor2); i++) {
            valor = (mayor * i);

            if ((valor % menor1) == 0 && (valor % menor2) == 0) {
              cout << "El mínimo común múltiplo es " << valor << endl;
              break;
            }
          }
        }
      }
    }
  }
  }
}

int MCM(int num1, int num2) {
  int minimoComun = 0, rA = max(num1, num2), rB = min(num1, num2);

  minimoComun = ((rA / MCD(num1, num2)) * rB);

  return minimoComun;
}
