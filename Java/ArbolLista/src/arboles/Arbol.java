/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package arboles;

import java.util.ArrayList;
import java.util.List;
/**
 *
 * @author Usuario
 */
public class Arbol {
    public Node buscarRaiz(List<Node> lista) {
        for (Node listas : lista) {
            if (listas.getIdPadre() == 0) {
                return listas;
            }
        }
        
        return null;
    }
    
    public List<Node> buscarHijos(Node padre, List<Node> lista) {
        List<Node> listaHijos = new ArrayList<Node>();
        
        for (Node listas : lista) {
            if (listas.getIdPadre() == padre.getId()) {
                listaHijos.add(listas);
            }
        }
        
        return listaHijos;
    }
    
    public List<Node> eliminarPadre(Node padre, List<Node> lista) {
        int indice = lista.indexOf(padre);
        
        lista.remove(indice);
        
        return lista;
    } 
    
    public void recorerHijos(Node padre, List<Node> lista) {
        System.out.println("\nHijos del padre: " + padre.getNombre());
        
        for (Node listas : lista) {
            System.out.println(listas.toString());
        }
    }
    
    public void recorrerArbol(Node padre, List<Node> lista) {
        List<Node> listaHijos = buscarHijos(padre, lista);
        
        if (listaHijos.isEmpty()) {
            return;
        }
        
        recorerHijos(padre, listaHijos);
        lista = eliminarPadre(padre, lista);
        
        for (Node padre1 : listaHijos) {
            recorrerArbol(padre1, lista);
        }
    }
}
