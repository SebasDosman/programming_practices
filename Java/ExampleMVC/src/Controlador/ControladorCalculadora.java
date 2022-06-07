package Controlador;

import java.awt.event.*;
import Modelo.Calculadora;
import Vista.VistaCalculadora;
import Vista.VistaCalculadoraGUI;

//Se implementa la logica de los botones y he aqui la union entre la GUI y la logica
public class ControladorCalculadora implements ActionListener {
    VistaCalculadora vista;
    Calculadora calculadora;

    public ControladorCalculadora(VistaCalculadora vista, Calculadora calculadora) {
        this.vista = vista;
        this.calculadora = calculadora;
    }

    public void iniciar() {
        vista.iniciar(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO Auto-generated method stub
        int num1 = vista.setNumero1(0);
        int num2 = vista.setNumero2(0);

        if (e.getSource() == VistaCalculadoraGUI.suma) {
            String resultado = "El resultado de la suma es " + calculadora.sumar(num1, num2);
            vista.setResultado(resultado);
        } 

        if (e.getSource() == VistaCalculadoraGUI.resta) {
            String resultado = "El resultado de la resta es " + calculadora.restar(num1, num2);
            vista.setResultado(resultado);
        }

        if (e.getSource() == VistaCalculadoraGUI.multiplicacion) {
            String resultado = "El resultado de la multiplicacion es " + calculadora.multiplicar(num1, num2);
            vista.setResultado(resultado);
        }

        if (e.getSource() == VistaCalculadoraGUI.division) {
            String resultado = "El resultado de la division es " + calculadora.dividir(num1, num2);
            vista.setResultado(resultado);
        }
    }
}
