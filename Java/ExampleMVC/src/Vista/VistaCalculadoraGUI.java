package Vista;

import java.awt.*;
import javax.swing.*;
import Controlador.ControladorCalculadora;

//Toda la interfaz grafica se crea en la vista, he aqui entonces la GUI a utilizar
public class VistaCalculadoraGUI extends JFrame implements VistaCalculadora {
    ControladorCalculadora controlador;
    int numero1, numero2;
    Container contenedor;
    JTextArea campo1, campo2, campo3;
    JLabel etiqueta1, etiqueta2, etiqueta3;
    public static JButton suma, resta, multiplicacion, division;
    JPanel panel1, panel2, panel3, panel4;

    public VistaCalculadoraGUI() {
        contenedor = getContentPane();
        contenedor.setLayout(new GridLayout(4, 1));

        panel1 = new JPanel(new GridLayout(1, 2));
        etiqueta1 = new JLabel("Numero 1: ");
        panel1.add(etiqueta1);
        campo1 = new JTextArea();
        panel1.add(campo1);
        contenedor.add(panel1);

        panel2 = new JPanel(new GridLayout(1, 2));
        etiqueta2 = new JLabel("Numero 2: ");
        panel2.add(etiqueta2);
        campo2 = new JTextArea();
        panel2.add(campo2);
        contenedor.add(panel2);

        panel3 = new JPanel(new GridLayout(1, 2));
        etiqueta3 = new JLabel("Resultado: ");
        panel3.add(etiqueta3);
        campo3 = new JTextArea();
        panel3.add(campo3);
        contenedor.add(panel3);

        panel4 = new JPanel(new GridLayout(1, 4));
        suma = new JButton("Sumar");
        panel4.add(suma);
        resta = new JButton("Restar");
        panel4.add(resta);
        multiplicacion = new JButton("Multiplicar");
        panel4.add(multiplicacion);
        division = new JButton("Dividir");
        panel4.add(division);
        contenedor.add(panel4);

        setSize(500, 500);
        setVisible(true);
    }

    //Tambien se implementan los metodos para obtener los datos de la GUI
    @Override
    public int setNumero1(int num1) {
        // TODO Auto-generated method stub
        numero1 = Integer.parseInt(campo1.getText());
        return numero1;
    }

    @Override
    public int setNumero2(int num2) {
        // TODO Auto-generated method stub
        numero2 = Integer.parseInt(campo2.getText());
        return numero2;
    }

    @Override
    public void setResultado(String resultado) {
        // TODO Auto-generated method stub
        campo3.setText(resultado);
    }

    //Aqui se inicia controlador para poder manejar los ActionListener de cada uno de los botones
    @Override
    public void iniciar(ControladorCalculadora controlador) {
        // TODO Auto-generated method stub
        this.controlador = controlador;
        suma.addActionListener(controlador);
        resta.addActionListener(controlador);
        multiplicacion.addActionListener(controlador);
        division.addActionListener(controlador);
        setVisible(true);
    }
}
