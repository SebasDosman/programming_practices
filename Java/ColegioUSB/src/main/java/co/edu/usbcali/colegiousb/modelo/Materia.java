/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.colegiousb.modelo;
/**
 *
 * @author joseph
 */
public class Materia {
    private String nombre;
    private Empleado empleado[];
    private Estudiante estudiante[];
    private String contenido;
    private int grado;
    private String horario;

    public Materia(String nombre, Empleado empleado[], Estudiante estudiante[], String contenido, int grado, String horario) {
        this.nombre = nombre;
        this.empleado = empleado;
        this.estudiante = estudiante;
        this.contenido = contenido;
        this.grado = grado;
        this.horario = horario;
    }

    public Materia() {
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void getEmpleado() {
        for (int i = 0; i < empleado.length; i++) {
            System.out.println(empleado[i].toString());
        }
    }

    public void setEmpleado(Empleado empleado[]) {
        this.empleado = empleado;
    }

    public void getEstudiante() {
        for (int i = 0; i < estudiante.length; i++) {
            System.out.println(estudiante[i].toString());
        }
    }

    public void setEstudiantes(Estudiante estudiante[]) {
        this.estudiante = estudiante;
    }

    public String getContenido() {
        return contenido;
    }

    public void setContenido(String contenido) {
        this.contenido = contenido;
    }

    public int getGrado() {
        return grado;
    }

    public void setGrado(byte grado) {
        this.grado = grado;
    }

    public String getHorario() {
        return horario;
    }

    public void setHorario(String horario) {
        this.horario = horario;
    }

    @Override
    public String toString() {
        return "Materia{" + "nombre=" + nombre + ", empleado=" + empleado + ", estudiantes=" + estudiante + ", contenido=" + contenido + ", grado=" + grado + ", horario=" + horario + '}';
    }
}
