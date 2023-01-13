#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "operacion.h"

#define SIZE_ARRAY 8
#define ROWS_MATRIZ 3
#define COLS_MATRIZ 4

int *miArreglo;

int main(void) 
{
  int salida = 0;
  int salida1 = 0;
  int a=0;
  int b=0;
  int total = 0;
  char user[20];
  char contra[20];
  char user1[20] = "usuario123"; 
  char contra1[20] = "contra123";


  printf("Digite su usuario para ingresar al sistema\n");
  scanf("%c", &user[20]);
  printf("Digite la contraseña para ingresar al sistema\n");
  scanf("%c", &contra[20]);


  if (strcmp(user, user1)) {
    } if (strcmp(contra, contra1)) {
      printf("Elija una de las siguientes opciones\n");
      printf("1. Calculadora\n");
      printf("2. Ingresar a Arrays\n");
      printf("3. Salir\n");
      scanf("%d", &salida);
    
   } switch (salida){

        case 1:
          printf("Elija una de las siguientes opciones de la calculadora\n");
          printf("1. Suma\n");
          printf("2. Resta\n");
          printf("3. Multiplicacion\n");
          printf("4. Division\n");
          scanf("%d", &salida1);

          switch (salida1){

            case 1:
            printf("Ingrese el primer numero: ");
            scanf("%d",&a);
            printf("Ingrese el primer numero: ");
            scanf("%d",&b);

            total = suma(a,b);

            printf("El resultado de la suma es %d\n", total);
            break;  

            case 2:
            printf("Ingrese el primer numero: ");
            scanf("%d",&a);
            printf("Ingrese el primer numero: ");
            scanf("%d",&b);

            total = resta(a,b);

            printf("El resultado de la resta es %d\n", total);
            break;

            case 3:
            printf("Ingrese el primer numero: ");
            scanf("%d",&a);
            printf("Ingrese el primer numero: ");
            scanf("%d",&b);

            total = multiplicacion(a,b);

            printf("El resultado de la multiplicacion es %d\n", total);
            break;

            case 4:
            printf("Ingrese el primer numero: ");
            scanf("%d",&a);
            printf("Ingrese el primer numero: ");
            scanf("%d",&b);

            total = division(a,b);

            printf("El resultado de la division es %d\n", total);
            break;

            case 5: 
            printf("Vuelva pronto");

            default:
            printf("Ingresó una opcion no valida\n");
            break;
          }
    break;

    case 2:
         miArreglo = (int*)malloc(sizeof(int)*SIZE_ARRAY);

         for(int i =0;i<SIZE_ARRAY;i++){
           miArreglo[i]=0;
         }
         free(miArreglo);

         char **miMatriz;
         miMatriz = (char **)malloc(sizeof(char*) * ROWS_MATRIZ );

         for(int i = 0; i < ROWS_MATRIZ; i++) 
         {
         miMatriz[i] = (char *)malloc(sizeof(char)*COLS_MATRIZ);
         }

         miMatriz[0]="Hola";
         miMatriz[1]="Como";
         miMatriz[2]="Esta";

         for(int i=0;i<ROWS_MATRIZ;i++)
         {
          for(int j=0;j<COLS_MATRIZ;j++)
           {
           printf("%c\n",miMatriz[i][j]);
           }
           }
           free(miMatriz);
      break;

      case 3:
        printf("Vuelva pronto");
      break;
     } 
  return 0;
}
