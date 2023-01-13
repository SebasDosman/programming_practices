/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package arboles;

import java.text.ParseException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
/**
 *
 * @author usuario
 */
public class ArbolLista {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ParseException {
//        Instancia metodos Arbol
        Arbol arbol = new Arbol();
        
//        Instancias nodos
        Node node1 = new Node(1, "Menu 2", 3);
        Node node2 = new Node(2, "Menu 3", 3);
        Node node3 = new Node(3, "Home", 0);
        Node node4 = new Node(4, "a", 3);
        Node node5 = new Node(5, "b", 4);
        Node node6 = new Node(6, "Menu 1", 1);
        Node node7 = new Node(7, "c", 5);
        Node node8 = new Node(8, "d", 5);
        Node node9 = new Node(9, "e", 5);
        Node node10 = new Node(10, "f", 6);
        
//        Lista de arboles
        List<Node> listaArbol = new ArrayList<Node>();
        
//        Agregar nodos en lista
        listaArbol.add(node1);
        listaArbol.add(node2);
        listaArbol.add(node3);
        listaArbol.add(node4);
        listaArbol.add(node5);
        listaArbol.add(node6);
        listaArbol.add(node7);
        listaArbol.add(node8);
        listaArbol.add(node9);
        listaArbol.add(node10);
        
//        Buscar raiz
        Node raiz = arbol.buscarRaiz(listaArbol);
        System.out.println("\nNodo Raíz: " + raiz.toString());
        
//        Recorrer arbol
        arbol.recorrerArbol(raiz, listaArbol);
    }
}
