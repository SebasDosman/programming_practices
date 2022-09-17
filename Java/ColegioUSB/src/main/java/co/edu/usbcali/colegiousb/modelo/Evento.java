/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.colegiousb.modelo;

import co.edu.usbcali.colegiousb.tipoenum.TipoEvento;
/**
 *
 * @author joseph
 */
public class Evento {
    private TipoEvento evento;
    private Materia materia[];
    private String ubicacion;
    private int duracion;

    public Evento(TipoEvento evento, Materia materia[], String ubicacion, int duracion) {
        this.evento = evento;
        this.materia = materia;
        this.ubicacion = ubicacion;
        this.duracion = duracion;
    }

    public Evento() {
        this.materia = null;
    }

    public TipoEvento getEvento() {
        return evento;
    }

    public void setEvento(TipoEvento evento) {
        this.evento = evento;
    }

    public void getMateria() {
        for (int i = 0; i < materia.length; i++) {
            System.out.println(materia[i].toString());
        }
    }

    public void setMateria(Materia materia[]) {
        this.materia = materia;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public void setUbicacion(String ubicacion) {
        this.ubicacion = ubicacion;
    }

    public int getDuracion() {
        return duracion;
    }

    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    @Override
    public String toString() {
        return "Evento{" + "evento=" + evento + ", materia=" + materia + ", ubicacion=" + ubicacion + ", duracion=" + duracion + '}';
    }
}
