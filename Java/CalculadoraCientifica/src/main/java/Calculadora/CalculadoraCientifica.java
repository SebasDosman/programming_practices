/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Calculadora;
import Operaciones.*;
import javax.swing.JOptionPane;
/**
 *
 * @author JUAN SEBASTIAN DOSMAN
 */
public class CalculadoraCientifica {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int opcion = 0;
        
        Operaciones operaciones = new Operaciones();
        
        JOptionPane.showMessageDialog(null, "Bienvenid@ al sistema");
        
        do {
            try {
            opcion = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite una de las isguientes opciones: \n"
                    + "1. Suma \n"
                    + "2. Resta \n"
                    + "3. Multiplicación \n"
                    + "4. División \n"
                    + "5. Logaritmo \n"
                    + "6. Seno \n"
                    + "7. Coseno \n"
                    + "8. Tangente \n"
                    + "9. Raíz Cuadrada \n"
                    + "10. Porcentaje \n"
                    + "11. Salir"));
            } catch(Exception e) {
                JOptionPane.showMessageDialog(null, "Debes digitar una de las opciones correspondientes", "Calculadora Cientifica", JOptionPane.ERROR_MESSAGE);
            }
            
            switch(opcion) {
                case 1:
                    Operaciones.Suma();
                break;
                case 2:
                    Operaciones.Resta();
                break;
                case 3:
                    Operaciones.Multiplicacion();
                break;
                case 4:
                    Operaciones.Division();
                break;
                case 5:
                    Operaciones.Logaritmo();
                break;
                case 6:
                    Operaciones.Seno();
                break;
                case 7:
                    Operaciones.Coseno();
                break;
                case 8:
                    Operaciones.Tangente();
                break;
                case 9:
                    Operaciones.raizCuadrada();
                break;
                case 10:
                    Operaciones.Porcentaje();
                break;
                case 11:
                    JOptionPane.showMessageDialog(null, "Gracias por usar el programa", "Calculadora Cientifica", JOptionPane.INFORMATION_MESSAGE);
                break;
                default:
                    JOptionPane.showMessageDialog(null, "Debes digitar una de las opciones correspondientes", "Calculadora Cientifica", JOptionPane.ERROR_MESSAGE);
            }
        } while(opcion != 11);
    }
}
