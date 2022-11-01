/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package co.edu.usbcali.jugadores;

import java.util.Collections;
import java.util.Comparator;

/**
 *
 * @author usuario
 */

public class ProyectoListas {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
//        Instancia de la lista
        Lista lista = new Lista();
        
//        Instancias  de los jugadores iniciales
        lista.agregarJugadorInicial(new Jugador(1, "Mailo Malevolo", "Portero"));
        lista.agregarJugadorInicial(new Jugador(2, "Mailo Bonilla", "Central"));
        lista.agregarJugadorInicial(new Jugador(3, "Mailo Bonilla", "Central"));
        lista.agregarJugadorInicial(new Jugador(4, "Mailo Bonilla", "Lateral"));
        lista.agregarJugadorInicial(new Jugador(5, "Mailo Bonilla", "Lateral"));
        lista.agregarJugadorInicial(new Jugador(6, "Mailo Bonilla", "Mediocampista"));
        lista.agregarJugadorInicial(new Jugador(7, "Mailo Bonilla", "Mediocampista"));
        lista.agregarJugadorInicial(new Jugador(8, "Mailo Bonilla", "Extremo"));
        lista.agregarJugadorInicial(new Jugador(9, "Mailo Bonilla", "Extremo"));
        lista.agregarJugadorInicial(new Jugador(10, "Mailo Bonilla", "Delantero"));
        lista.agregarJugadorInicial(new Jugador(11, "Mailo Bonilla", "Delantero"));
        
//        Instancias de los jugadores suplentes
        lista.agregarJugadorSuplente(new Jugador(12, "Mailo Cabron", "Mediocampista"));
        lista.agregarJugadorSuplente(new Jugador(13, "Mailo Bonilla", "Mediocampista"));
        lista.agregarJugadorSuplente(new Jugador(14, "Mailo Bonilla", "Extremo"));
        lista.agregarJugadorSuplente(new Jugador(15, "Mailo Bonilla", "Extremo"));
        lista.agregarJugadorSuplente(new Jugador(16, "Mailo Bonilla", "Delantero"));
        lista.agregarJugadorSuplente(new Jugador(17, "Mailo Bonilla", "Delantero"));
        
//        Impresion de los jugadores iniciales y suplentes
        lista.imprimirJugadoresIniciales();
        lista.imprimirJugadoresSuplentes();
        
//        Cambio de jugadores
        lista.cambioJugadores(2, 13);
        
//        Impresion de los jugadores iniciales y suplentes
        lista.imprimirJugadoresIniciales();
        lista.imprimirJugadoresSuplentes();
        
//        Ordenamiento inverso de los jugadores iniciales y suplentes
        lista.ordenarJugadoresIniciales();
        lista.ordenarJugadoresSuplentes();
        
//        Impresion de los jugadores iniciales y suplentes
        lista.imprimirJugadoresIniciales();
        lista.imprimirJugadoresSuplentes();
    }
}
