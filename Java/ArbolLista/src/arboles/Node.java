/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package arboles;

/**
 *
 * @author usuario
 */
public class Node {
    private int id;
    private String nombre;
    private int idPadre;

    public Node(int id, String nombre, int idPadre) {
        this.id = id;
        this.nombre = nombre;
        this.idPadre = idPadre;
    }

    public Node() {
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getIdPadre() {
        return idPadre;
    }

    public void setIdPadre(int idPadre) {
        this.idPadre = idPadre;
    }

    @Override
    public String toString() {
        return "Node{" + "id=" + id + ", nombre=" + nombre + ", idPadre=" + idPadre + '}';
    }
}
