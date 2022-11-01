/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package co.edu.usbcali.lecturaarchivo;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author joseph
 */

public class LecturaArchivo {
    public static void main(String[] args) {
        try (FileWriter escritura = new FileWriter("test.txt",true)) { 
            
            escritura.write("Estoy escribiendo \n"); 
        } catch (IOException ex) {
            Logger.getLogger(LecturaArchivo.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        String contenido = "";
        int caracter;
        
        try {
            FileReader leer = new FileReader("test.txt");
            
            while ((caracter=leer.read()) != -1) {
                contenido += (char)caracter;
            }
        } catch (FileNotFoundException ex) {
            Logger.getLogger(LecturaArchivo.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(LecturaArchivo.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        System.out.println("El contenido es: " + contenido);
    }
}
