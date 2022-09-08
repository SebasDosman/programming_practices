/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Operaciones;
import javax.swing.JOptionPane;
/**
 *
 * @author JUAN SEBASTIAN DOSMAN
 */
public class Operaciones {
    public static void Suma() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
            num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            acu += num;
        }
        
        JOptionPane.showMessageDialog(null, "La suma es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    public static void Resta() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                acu -= num;
            }
     
            JOptionPane.showMessageDialog(null, "La resta es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void Multiplicacion() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                acu *= num;
            }
     
            JOptionPane.showMessageDialog(null, "La multiplicación es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void Division() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                if (i == 1) {
                    acu += num;
                } else {
                    acu /= num;    
                }
                
                if (num == 0 && i >= 2) {
                    JOptionPane.showMessageDialog(null, "No es posible realizar una división entre 0", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
                }    
            }
     
            JOptionPane.showMessageDialog(null, "La división es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void Logaritmo() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                acu = Math.log(num);
                
                JOptionPane.showMessageDialog(null, "El logaritmo es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void Seno() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                acu = Math.sin(num);
                
                JOptionPane.showMessageDialog(null, "El seno es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void Coseno() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                acu = Math.cos(num);
                
                JOptionPane.showMessageDialog(null, "El coseno es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void Tangente() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                acu = Math.tan(num);
                
                JOptionPane.showMessageDialog(null, "La tangente es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void raizCuadrada() {
        int cant = 0;
        double num = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                acu = Math.sqrt(num);
                
                JOptionPane.showMessageDialog(null, "La raíz cuadrada es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
    
    public static void Porcentaje() {
        int cant = 0;
        double num1 = 0, num2 = 0, acu = 0;
        
        try {
            cant = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la cantidad de números a operar", "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
            
            for(int i = 1; i <= cant; i++) {
                num1 = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                num2 = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite el número de porcentaje a sacar " + i, "Calculadora Científica", JOptionPane.QUESTION_MESSAGE));
                
                num2 /= 100;
                acu = num1 * num2;
                
                JOptionPane.showMessageDialog(null, "El porcentaje es igual a: " + acu, "Calculadora Científica", JOptionPane.WARNING_MESSAGE);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Debes digitar un número a operar", "Calculadora Científica", JOptionPane.ERROR_MESSAGE);
        } 
    }
}
