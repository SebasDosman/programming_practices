/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.tree;
/**
 *
 * @author joseph
 */
public class Node {
    private String nombre;
    private String ruta;

    public Node(String nombre, String ruta) {
        this.nombre = nombre;
        this.ruta = ruta;
    }

    public Node() {
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getRuta() {
        return ruta;
    }

    public void setRuta(String ruta) {
        this.ruta = ruta;
    }
}
