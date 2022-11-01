/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.jugadores;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 *
 * @author usuario
 */

public class Lista {
    private List<Jugador> jugadoresIniciales;
    private List<Jugador> jugadoresSuplentes;

    public Lista() {
        this.jugadoresIniciales = new ArrayList<Jugador>();
        this.jugadoresSuplentes = new ArrayList<Jugador>();
    }
    
    public void agregarJugadorInicial(Jugador jugador) {
        this.jugadoresIniciales.add(jugador);
    }
    
    public void agregarJugadorSuplente(Jugador jugador) {
        this.jugadoresSuplentes.add(jugador);
    }
    
    public void imprimirJugadoresIniciales() {
        System.out.println("\n Jugadores Iniciales: ");
        
        for (int i = 0; i < this.jugadoresIniciales.size(); i++) {
            System.out.println(this.jugadoresIniciales.get(i).toString());
        }
    }
    
    public void imprimirJugadoresSuplentes() {
        System.out.println("\n Jugadores Suplentes: ");
        
        for (int i = 0; i < this.jugadoresSuplentes.size(); i++) {
            System.out.println(this.jugadoresSuplentes.get(i).toString());
        }
    }
    
    public int buscarJugador(int numeroJugador, List<Jugador> lista) {
        int i = 0;
        
        for (i = 0; i < lista.size(); i++) {
            if (lista.get(i).getNumero() == numeroJugador) {
                break;
            }
        }
        
        return i;
    }
    
    public void cambioJugadores(int numeroTitular, int numeroSuplente) {        
        int indiceTitular = buscarJugador(numeroTitular, this.jugadoresIniciales);
        Jugador jugadorInicialCambio = this.jugadoresIniciales.get(indiceTitular);
        this.jugadoresIniciales.remove(indiceTitular);
        
        int indiceSuplente = buscarJugador(numeroSuplente, this.jugadoresSuplentes);
        Jugador jugadorSuplenteCambio = this.jugadoresSuplentes.get(indiceSuplente);
        this.jugadoresSuplentes.remove(indiceSuplente);
        
        jugadoresIniciales.add(indiceTitular, jugadorSuplenteCambio);
        jugadoresSuplentes.add(indiceSuplente, jugadorInicialCambio);
    }
    
    public void ordenarJugadoresIniciales() {
        Collections.sort(this.jugadoresIniciales);
    }
    
    public void ordenarJugadoresInicialesRevez() {
        Collections.sort(this.jugadoresIniciales);
        Collections.reverse(this.jugadoresIniciales);
    }
    
    public void ordenarJugadoresSuplentes() {
        Collections.sort(this.jugadoresSuplentes);
    }
    
    public void ordenarJugadoresSuplentesRevez() {
        Collections.sort(this.jugadoresSuplentes);
        Collections.reverse(this.jugadoresSuplentes);
    }
}
