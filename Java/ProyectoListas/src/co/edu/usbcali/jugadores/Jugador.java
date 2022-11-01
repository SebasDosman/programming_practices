/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.jugadores;

import java.util.Collections;
import java.util.Comparator;

/**
 *
 * @author usuario
 */
public class Jugador implements Comparable<Jugador> {
    private int numero;
    private String nombre;
    private String posicion;

    public Jugador(int numero, String nombre, String posicion) {
        this.numero = numero;
        this.nombre = nombre;
        this.posicion = posicion;
    }

    public Jugador() {
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getPosicion() {
        return posicion;
    }

    public void setPosicion(String posicion) {
        this.posicion = posicion;
    }

    @Override
    public String toString() {
        return "Jugador {" + "numero = " + numero + ", nombre = " + nombre + ", posicion = " + posicion + '}';
    }

    @Override
    public int compareTo( Jugador jugador ) {
        int numeroJugador = Integer.compare(numero, jugador.numero);
        
        if ( numeroJugador != 0 ) {
            return numeroJugador;
            } if ( nombre == null ) {
                if ( jugador.nombre == null ) {
                    return 0;
                } else {
                    return 1;
                }
            } if ( jugador.nombre == null ) {
                return 1;
        }
        
        return nombre.compareToIgnoreCase(jugador.nombre);
    }
}
