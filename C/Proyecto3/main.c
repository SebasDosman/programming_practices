#include <stdio.h>

int main(void) {
  int miEntero = 5;
  int a=0;
  int b=0;
  int suma=0;
  

  //Print Message
  
  printf("Direccion de memoria %p\n",&miEntero);
  printf ("Characters: %c %c \n", 'a', 65);
  printf ("Decimals: %d %ld\n", 1977, 650000L);
  printf ("Preceding with blanks: %10d \n", 1977);
  printf ("Preceding with zeros: %010d \n", 1977);
  printf ("Some different radices: %d %x %o %#x %#o \n", 100, 100, 100, 100, 100);
  printf ("floats: %4.2f %+.0e %E \n", 3.1416, 3.1416, 3.1416);
  printf ("Width trick: %*d \n", 5, 10);
  printf ("%s \n", "A string");

  //Get Info
  printf("\n\nIngrese el primer valor: ");
  scanf("%i",&a);
  printf("\nIngrese el segundo valor: ");
  scanf("%i",&b);

  suma = a + b;
  printf("la suma es: %d", suma);

  //Estructuras de Control

  /*if(suma > 50 || suma < 30){
      printf("\nEs mayor que 50 o menor que 30");
  }*/

  if(suma > 50 && suma <= 60)
  {
    printf("\nEs mayor que 50 y menor que 60");
  }else
  {
    printf("\nNo se cumple la condicion");
  }

  switch(suma)
  {
      case 1:
        printf("\nLa suma es %i",suma);
        break;
      case 2:
        printf("\nLa suma es %i",suma);
        break;
      case 5:
        printf("\nLa suma es %i",suma);
        break;
      default:      
       break;
  }

  return 0;
}