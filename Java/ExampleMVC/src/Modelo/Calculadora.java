package Modelo;

//Se implementa la interface para trabajar con los metodos de la misma
public class Calculadora implements CalculadoraMetodos {
    @Override
    public int sumar(int num1, int num2) {
        // TODO Auto-generated method stub
        return num1 + num2;
    }

    @Override
    public int restar(int num1, int num2) {
        // TODO Auto-generated method stub
        return num1 - num2;
    }

    @Override
    public int multiplicar(int num1, int num2) {
        // TODO Auto-generated method stub
        return num1 * num2;
    }

    @Override
    public int dividir(int num1, int num2) {
        // TODO Auto-generated method stub
        return num1 / num2;
    }
}
