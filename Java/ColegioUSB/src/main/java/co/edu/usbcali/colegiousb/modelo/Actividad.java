/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.colegiousb.modelo;

import co.edu.usbcali.colegiousb.tipoenum.TipoActividad;
import java.util.Date;
/**
 *
 * @author joseph
 */
public class Actividad {
    private TipoActividad actividad;
    private double calificacion;
    private int grado;
    private Date fecha;
    private Materia materia;

    public Actividad(TipoActividad actividad, double calificacion, int grado, Date fecha, Materia materia) {
        this.actividad = actividad;
        this.calificacion = calificacion;
        this.grado = grado;
        this.fecha = fecha;
        this.materia = materia;
    }

    public Actividad() {
    }

    public TipoActividad getActividad() {
        return actividad;
    }

    public void setActividad(TipoActividad actividad) {
        this.actividad = actividad;
    }

    public double getCalificacion() {
        return calificacion;
    }

    public void setCalificacion(double calificacion) {
        this.calificacion = calificacion;
    }

    public int getGrado() {
        return grado;
    }

    public void setGrado(byte grado) {
        this.grado = grado;
    }

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    public Materia getMateria() {
        return materia;
    }

    public void setMateria(Materia materia) {
        this.materia = materia;
    }

    @Override
    public String toString() {
        return "Actividad{" + "actividad=" + actividad + ", calificacion=" + calificacion + ", grado=" + grado + ", fecha=" + fecha + ", materia=" + materia + '}';
    }
}
