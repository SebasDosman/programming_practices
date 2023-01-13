/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package arbolbinario;
/**
 *
 * @author usuario
 */
public class Nodo {
    private Object dato;
    private Nodo izq;
    private Nodo der;
    
    public Nodo(Object dato){
        this.dato = dato;
        izq = null;
        der = null;
    }
    
    public Nodo() {
    }
    
    public boolean esHoja(){
        return(izq == null && der == null);
    }
    
    public Object getDato() {
        return dato;
    }

    public void setDato(Object dato) {
        this.dato = dato;
    }

    public Nodo getIzq() {
        return izq;
    }

    public void setIzq(Nodo izq) {
        this.izq = izq;
    }

    public Nodo getDer() {
        return der;
    }

    public void setDer(Nodo der) {
        this.der = der;
    }
}
