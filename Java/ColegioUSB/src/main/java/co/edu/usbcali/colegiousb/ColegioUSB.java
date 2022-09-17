/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package co.edu.usbcali.colegiousb;

import co.edu.usbcali.colegiousb.modelo.*;
import co.edu.usbcali.colegiousb.tipoenum.*;
import java.text.SimpleDateFormat;
import java.util.Date;
/**
 *
 * @author joseph
 */
public class ColegioUSB {
    
    public static void main(String[] args) {
        SimpleDateFormat date = new SimpleDateFormat("dd/MM/yyyy");
        
        Estudiante estudiante1 = new Estudiante(1234567, "Juan", 18, TipoSexo.MASCULINO, 9, "Buzo");
        Estudiante estudiante2 = new Estudiante(5689090, "Carlos", 16, TipoSexo.MASCULINO, 10, "Buzo");
        Estudiante estudiante3 = new Estudiante(1237690, "Maria", 15, TipoSexo.FEMENINO, 11, "Blusa");
        
        Empleado empleado1 = new Empleado(1234567, "Diego", 26, TipoSexo.MASCULINO, TipoRol.PROFESOR, 400000);
        Empleado empleado2 = new Empleado(3847013, "Mariana", 30, TipoSexo.FEMENINO, TipoRol.PROFESOR, 800000);
        Empleado empleado3 = new Empleado(3085308, "Daniel", 28, TipoSexo.MASCULINO, TipoRol.PROFESOR, 900000);
        
        Estudiante estudiantes[] = {
            estudiante1,
            estudiante2,
            estudiante3
        };
        
        Empleado empleados[] = {
            empleado1,
            empleado2,
            empleado3
        };
        
        Colegio comfandi = new Colegio(909, empleados, estudiantes, "Cali");
        
        Materia matematicas = new Materia("Matematicas", empleados, estudiantes, "Sumas y Restas", 10, "");
        
        Materia materias[] = {
            matematicas
        };
        
        Evento evento = new Evento(TipoEvento.FESTIVIDAD, materias, "Cali", 120);
        
        Actividad quiz = new Actividad(TipoActividad.QUIZ, 4.5, 10, new Date(2004, 05, 12), matematicas);
    }
}
