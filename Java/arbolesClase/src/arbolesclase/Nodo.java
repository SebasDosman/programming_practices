/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package arbolesclase;

/**
 *
 * @author mac20
 */
public class Nodo {
    
    private int  id, idPadre ;
    private String  nombre   ;

    
    public Nodo() {
    }

    public Nodo( int id, String nombre, int idPadre ) {
        this.id         = id        ;
        this.idPadre    = idPadre   ;
        this.nombre     = nombre    ;
    }

    public int getId() {
        return id;
    }

    public int getIdPadre() {
        return idPadre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setIdPadre(int idPadre) {
        this.idPadre = idPadre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Nodo{");
        sb.append("id=").append(id);
        sb.append(", idPadre=").append(idPadre);
        sb.append(", nombre=").append(nombre);
        sb.append('}');
        return sb.toString();
    }
    
    
}
