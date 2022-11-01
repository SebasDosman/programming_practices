/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.tree;

import java.util.ArrayList;
import java.util.List;
/**
 *
 * @author joseph
 */
public class Tree {
    private Node padre;
    private List<Node> hijos;

    public Tree(Node padre, List<Node> hijos) {
        this.padre = padre;
        this.hijos = new ArrayList<Node>();
    }

    public Tree() {
    }

    public Node getPadre() {
        return padre;
    }

    public void setPadre(Node padre) {
        this.padre = padre;
    }

    public List<Node> getHijos() {
        return hijos;
    }

    public void setHijos(List<Node> hijos) {
        this.hijos = hijos;
    }
}
