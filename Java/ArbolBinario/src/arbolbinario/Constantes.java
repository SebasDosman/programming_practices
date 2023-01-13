/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package arbolbinario;

import javax.swing.JOptionPane;
/**
 *
 * @author Usuario
 */
public class Constantes {
    public void opcionesMenu() {
        JOptionPane.showMessageDialog(null, "1. Recorrido In - Orden" + 
                                                    "\n2. Recorrido Pre - Orden" +
                                                    "\n3. Recorrido Post - Orden" +
                                                    "\n4. Total de nodos" +
                                                    "\n-1. Salir", "Menú",JOptionPane.INFORMATION_MESSAGE);
    }
    
    public int escogerOpcion() {
        int opcion = 0;
        
        try {
            opcion = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la opción correspondiente", "Menú",JOptionPane.INFORMATION_MESSAGE));
        } catch(Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "Menú",JOptionPane.ERROR_MESSAGE);
        }
        
        return opcion;
    }
    
    public void mensajeDespedida() {
        JOptionPane.showMessageDialog(null, "Gracias por usar el programa", "Menú",JOptionPane.INFORMATION_MESSAGE);
    }
    
    public void mensajeError() {
        JOptionPane.showMessageDialog(null, "Debes digitar una opción correpondiente", "Menú",JOptionPane.ERROR_MESSAGE);
    }
    
    public void imprimirMensaje(String mensaje) {
        JOptionPane.showMessageDialog(null, mensaje, "Recorridos",JOptionPane.INFORMATION_MESSAGE);
    }
}
