#include <iostream>

using namespace std;

int main() {
  for (int va1 = 0; va1 < 10; va1++) {
		for (int va2 = 0; va2 < 10; va2++) {
			for (int va3 = 0; va3 < 10; va3++) {
				for (int va4 = 0; va4 < 10; va4++) {
					for (int va5 = 0; va5 < 10; va5++) {
            cout << " ";

            if (va1 == 3) {
	            cout << "E" << "-";
            } else {
	            cout << va1 << "-";	
            } if (va2 == 3) {
	            cout << "E" << "-";
            } else {
	            cout << va2 << "-";	
            } if (va3 == 3) {
	            cout << "E" << "-";
            } else {
	            cout << va3 << "-";	
            } if (va4 == 3) {
	            cout << "E" << "-";
            } else {
	            cout << va4 << "-";	
            } if (va5 == 3) {
	            cout << "E";
            } else {
              cout << va5;	
            }

            cout << "\n";
					}
        }
			}
		}
	}
}