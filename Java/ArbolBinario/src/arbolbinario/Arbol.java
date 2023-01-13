/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package arbolbinario;
/**
 *
 * @author usuario
 */
public class Arbol {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
//        Instancia del arbol binario
        ArbolBinario arbolBinario = new ArbolBinario("Arbol");
        
//        Instancia de las constantes
        Constantes constantes = new Constantes();
        
//        Instancia de los nodos
        Nodo raiz = new Nodo("Raiz"); Nodo nodo1 = new Nodo("Nodo 1"); Nodo nodo2 = new Nodo("Nodo 2"); Nodo nodo3 = new Nodo("Nodo 3"); Nodo nodo4 = new Nodo("Nodo 4"); Nodo nodo5 = new Nodo("Nodo 5"); Nodo nodo6 = new Nodo("Nodo 6"); Nodo nodo7 = new Nodo("Nodo 7"); Nodo nodo8 = new Nodo("Nodo 8"); Nodo nodo9 = new Nodo("Nodo 9"); Nodo nodo10 = new Nodo("Nodo 10"); Nodo nodo11 = new Nodo("Nodo 11"); Nodo nodo12 = new Nodo("Nodo 12"); Nodo nodo13 = new Nodo("Nodo 13"); Nodo nodo14 = new Nodo("Nodo 14"); Nodo nodo15 = new Nodo("Nodo 15"); Nodo nodo16 = new Nodo("Nodo 16"); Nodo nodo17 = new Nodo("Nodo 17"); Nodo nodo18 = new Nodo("Nodo 18"); Nodo nodo19 = new Nodo("Nodo 19"); Nodo nodo20 = new Nodo("Nodo 20"); Nodo nodo21 = new Nodo("Nodo 21"); Nodo nodo22 = new Nodo("Nodo 22"); Nodo nodo23 = new Nodo("Nodo 23"); Nodo nodo24 = new Nodo("Nodo 24"); Nodo nodo25 = new Nodo("Nodo 25"); Nodo nodo26 = new Nodo("Nodo 26"); Nodo nodo27 = new Nodo("Nodo 27"); Nodo nodo28 = new Nodo("Nodo 28"); Nodo nodo29 = new Nodo("Nodo 29"); Nodo nodo30 = new Nodo("Nodo 30");
        
//        Asignacion de hijos por cada padre 
        raiz.setIzq(nodo1); raiz.setDer(nodo2); nodo1.setIzq(nodo3); nodo1.setDer(nodo4); nodo2.setIzq(nodo5); nodo2.setDer(nodo6); nodo3.setIzq(nodo7); nodo3.setDer(nodo8); nodo4.setIzq(nodo9); nodo4.setDer(nodo10); nodo5.setIzq(nodo11); nodo5.setDer(nodo12); nodo6.setIzq(nodo13); nodo6.setDer(nodo14); nodo7.setIzq(nodo15); nodo7.setDer(nodo16); nodo8.setIzq(nodo17); nodo8.setDer(nodo18); nodo9.setIzq(nodo19); nodo9.setDer(nodo20); nodo10.setIzq(nodo21); nodo10.setDer(nodo22); nodo11.setIzq(nodo23); nodo11.setDer(nodo24); nodo12.setIzq(nodo25); nodo12.setDer(nodo26); nodo13.setIzq(nodo27); nodo13.setDer(nodo28); nodo14.setIzq(nodo29); nodo14.setDer(nodo30);
        
//        Asignacion de la raiz al arbol
        arbolBinario.setRaiz(raiz);
        
//        Menu
        constantes.opcionesMenu();
        int opcion = constantes.escogerOpcion(); 
        
//        Opciones del menu
        while(opcion != -1) {
            switch (opcion) {
                case 1:
                    constantes.imprimirMensaje("Recorrido In - Orden: \n" + arbolBinario.getElementosInOrden());
                    
                    constantes.opcionesMenu();
                    opcion = constantes.escogerOpcion();
                case 2:
                    constantes.imprimirMensaje("Recorrido Pre - Orden: \n" + arbolBinario.getElementosPreOrden());
                    
                    constantes.opcionesMenu();
                    opcion = constantes.escogerOpcion();
                case 3:
                    constantes.imprimirMensaje("Recorrido Post - Orden: \n" + arbolBinario.getElementosPostOrden());
                    
                    constantes.opcionesMenu();
                    opcion = constantes.escogerOpcion();
                case 4:
                    constantes.imprimirMensaje("Total Nodos: " + arbolBinario.getTotal());
                    
                    constantes.opcionesMenu();
                    opcion = constantes.escogerOpcion();
                case -1:
                    constantes.mensajeDespedida();
                    
                    break;
                default:
                    constantes.mensajeError();
                    
                    constantes.opcionesMenu();
                    opcion = constantes.escogerOpcion();
            }
        }
    }
}
