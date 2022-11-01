#include <stdio.h>
#include <stdlib.h>

#define SIZE_ARRAY 8

#define ROWS_MATRIZ 3
#define COLS_MATRIZ 4

int main(void) {

  //Vector
  int *miArreglo;
  //Revamos la cantidad memoria
  miArreglo = (int*)malloc(sizeof(int)*SIZE_ARRAY);

  //recorremos el vector e inicializamos todas las posiciones con 0
  for(int i =0;i<SIZE_ARRAY;i++){
    miArreglo[i]=0;
  }
  //liberamos la memoria
  free(miArreglo);

  //Matrices
  char **miMatriz;
  //Reservamos la memoria de las filas de la matriz
  miMatriz = (char **)malloc(sizeof(char*) * ROWS_MATRIZ );

  //Reservamos la memoria de las columas de la matriz
  for(int i = 0; i < ROWS_MATRIZ; i++) 
  {
    miMatriz[i] = (char *)malloc(sizeof(char)*COLS_MATRIZ);
  }

  //llenamos con datos nuestra matriz
  miMatriz[0]="Hola";
  miMatriz[1]="Como";
  miMatriz[2]="Esta";

  for(int i=0;i<ROWS_MATRIZ;i++)
  {
    for(int j=0;j<COLS_MATRIZ;j++)
    {
      printf("%c",miMatriz[i][j]);
    }
    printf(" ");
  }



  return 0;
}