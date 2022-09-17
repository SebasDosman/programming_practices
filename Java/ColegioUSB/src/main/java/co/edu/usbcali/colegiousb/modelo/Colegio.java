/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.colegiousb.modelo;
/**
 *
 * @author joseph
 */
public class Colegio {
    private int salon;
    private Empleado empleado[];
    private Estudiante estudiante[];
    private String ubicacion;

    public Colegio(int salon, Empleado empleado[], Estudiante estudiante[], String ubicacion) {
        this.salon = salon;
        this.empleado = empleado;
        this.estudiante = estudiante;
        this.ubicacion = ubicacion;
    }

    public Colegio() {
    }

    public int getSalon() {
        return salon;
    }

    public void setSalon(int salon) {
        this.salon = salon;
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

    public void setEstudiante(Estudiante estudiante[]) {
        this.estudiante = estudiante;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public void setUbicacion(String ubicacion) {
        this.ubicacion = ubicacion;
    }

    @Override
    public String toString() {
        return "Colegio{" + "salon=" + salon + ", empleado=" + empleado + ", estudiante=" + estudiante + ", ubicacion=" + ubicacion + '}';
    }
}
