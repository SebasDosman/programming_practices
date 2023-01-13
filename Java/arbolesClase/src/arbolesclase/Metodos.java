/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package arbolesclase;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author mac20
 */
public class Metodos {
    
//    Listo
    public Nodo obtenerRaiz( List<Nodo> listNodo ){
        
        for ( Nodo elemento: listNodo ) {
            
            if( elemento.getIdPadre() == 0 ) return elemento;
        }
        
        return null;
    };
    
    
//    Listo
    public List<Nodo> encontrarHijos( Nodo padre, List<Nodo> listNodos ){
        
        List<Nodo> listHijos = new ArrayList<Nodo>();
        
        for( Nodo elemento: listNodos ){
            
            if( elemento.getIdPadre() == padre.getId() ) listHijos.add( elemento );
        }
        
        return listHijos;
        
    }
    
//    Listo
    public void imprimirHijos( Nodo padre, List<Nodo> listHijos ){
        
        System.out.println("\n\nHijos de " + padre.getNombre() + "\n" );
        
        for( Nodo hijo: listHijos ){
            System.out.println( hijo.toString() );
        }
    }
    
    
    public List<Nodo> eliminarPadreLista( Nodo Padre, List<Nodo> listNodos ){
        
        int index = listNodos.indexOf(Padre );
        listNodos.remove( index );
        
        return listNodos;
    }
    
    
    public void recorrerLista( Nodo padre, List<Nodo> listNodos ){
        
        List<Nodo> listHijos = encontrarHijos(padre, listNodos);
        
        
        if( listHijos.size() == 0 ) return;
        
        
        imprimirHijos( padre , listHijos);
        listNodos = eliminarPadreLista(padre, listNodos);
        
        
        //En este momento tenemos una lista sin el padre, solo los hijos
        //Repetiremos el proceso con cada hijo que es raiz de subarbol
        for( Nodo hijo: listHijos ){
            recorrerLista( hijo, listNodos);
        }
    }
}
