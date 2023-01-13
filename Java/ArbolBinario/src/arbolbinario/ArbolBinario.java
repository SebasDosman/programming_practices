/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package arbolbinario;
/**
 *
 * @author usuario
 */
public class ArbolBinario {
    private Nodo raiz;
    private String nombre;
    private int contadorizq, contadorder, contadortotalnodos;

    public ArbolBinario(String nombre){
        this.nombre = nombre;
        this.raiz = null;
        this.contadorizq = 0;
        this.contadorder = 0;
    }
    
    public ArbolBinario() {
    }
    
    public Nodo getRaiz() {
        return raiz;
    }
    
    public void setRaiz(Nodo raiz) {
        this.raiz = raiz;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public boolean esVacio() {
        if (raiz == null) {
            return true;
        } else {
            return false;
        }
    }
    
    public int getContadorizq() {
        return contadorizq;
    }

    public void setContadorizq(int contadorizq) {
        this.contadorizq = contadorizq;
    }

    public int getContadorder() {
        return contadorder;
    }

    public void setContadorder(int contadorder) {
        this.contadorder = contadorder;
    }

    public int getContadortotalnodos() {
        return contadortotalnodos;
    }

    public void setContadortotalnodos(int contadortotalnodos) {
        this.contadortotalnodos = contadortotalnodos;
    }
    
    private String getElementosRec(Nodo aux){
        String elementos = " ";
        
        if (aux != null){
            elementos += aux.getDato() + " " +
            "Nodo Derecho: " + getElementosRec(aux.getDer()) + 
            "Nodo Izquierdo: " + getElementosRec(aux.getIzq());
        }
        
        return(elementos);
    }
    
    public String getElementos(){
        if (esVacio()){
            return("Arbol Vacio");
        }
        
        return(getElementosRec(raiz));
    }
    
    private String getPreOrden(Nodo aux) {
        String elementos = "";
        
        if (aux != null) {
            elementos += "\n" + aux.getDato();
            elementos += getPreOrden(aux.getIzq());
            elementos += getPreOrden(aux.getDer());
        }
        
        return (elementos);
    }
    
    public String getElementosPreOrden() {
        if (esVacio()) {
            return ("Arbol Vacio");
        } else {
            return (getPreOrden(raiz));
        }
    }
    
    private String getPostOrden(Nodo aux) {
        String elementos = "";
        
        if (aux != null) {
            elementos += getPostOrden(aux.getIzq());
            elementos += getPostOrden(aux.getDer());
            elementos += "\n" + aux.getDato();
        }
        
        return (elementos);
    }
    
    public String getElementosPostOrden() {
        if (esVacio()) {
            return ("Arbol Vacio");
        } else {
            return (getPostOrden(raiz));
        }
    }
    
    private String getInOrden(Nodo aux) {
        String elementos = "";
        
        if (aux != null) {
            elementos += getInOrden(aux.getIzq());
            elementos += "\n" + aux.getDato();
            elementos += getInOrden(aux.getDer());
        }
        
        return (elementos);
    }

    public String getElementosInOrden() {
        if (esVacio()) {
            return ("Arbol Vacio");
        } else {
            return (getInOrden(raiz));
        }
    }
    
    private void hallarAltura(Nodo aux) {
        if (aux != null) {
            if (aux.getDer() != null) {
                setContadorder(getContadorder() + 1);
                hallarAltura(aux.getDer());
            } if (aux.getIzq() != null) {
                setContadorizq(getContadorizq() + 1);
                hallarAltura(aux.getIzq());
            }
        }
    }
    
    public int getAltura() {
        hallarAltura(raiz);
        
        if (getContadorder() > getContadorizq()) {
            return (getContadorder() + 1);
        } else {
            return (getContadorizq() + 1);
        }
    }
    
    private int buscarTotalNodo(Nodo aux) {
        if (aux != null) {
            if (aux.getIzq() != null) {
                setContadortotalnodos(getContadortotalnodos() + 1);
                buscarTotalNodo(aux.getIzq());
            } if (aux.getDer() != null) {
                setContadortotalnodos(getContadortotalnodos() + 1);
                buscarTotalNodo(aux.getDer());
            }
        }
        
        return (getContadortotalnodos());
    }
    
    public int getTotal(){
        buscarTotalNodo(raiz);
        
        return(getContadortotalnodos() + 1);
    }
}
