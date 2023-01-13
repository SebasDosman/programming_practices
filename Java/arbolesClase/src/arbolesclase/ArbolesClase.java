/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package arbolesclase;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author mac20
 */
public class ArbolesClase {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
       Metodos metodos       = new Metodos()    ;
       List<Nodo> listaNodos = new ArrayList<>();
       
       
       Nodo menu2   = new Nodo( 1, "menu2"  , 3        );
       Nodo menu3   = new Nodo( 2, "menu3"  , 3        );
       Nodo raiz    = new Nodo( 3, "raiz"   , 0        );
       Nodo a       = new Nodo( 4, "a"      , 3        );
       Nodo b       = new Nodo( 5, "b"      , 4        );
       Nodo menu1   = new Nodo( 6, "menu1"  , 1        );
       Nodo c       = new Nodo( 7, "c"      , 5        );
       Nodo d       = new Nodo( 8, "d"      , 5        );
       Nodo e       = new Nodo( 9, "e"      , 5        );
       Nodo f       = new Nodo( 10, "f"     , 6        );

       listaNodos.add( menu2);
       listaNodos.add( menu3);
       listaNodos.add( raiz );
       listaNodos.add( a    );
       listaNodos.add( b    );
       listaNodos.add( menu1);
       listaNodos.add( c    );
       listaNodos.add( d    );
       listaNodos.add(   e    );
       listaNodos.add( f    );
       
        Nodo raizLista = metodos.obtenerRaiz( listaNodos );        
        metodos.recorrerLista( raizLista, listaNodos);
    }
}
