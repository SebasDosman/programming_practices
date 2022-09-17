/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.colegiousb.modelo;

import co.edu.usbcali.colegiousb.tipoenum.TipoSexo;
/**
 *
 * @author joseph
 */
public class Estudiante {
    private int id;
    private String nombre;
    private int edad;
    private TipoSexo sexo;
    private int grado;
    private String uniforme;

    public Estudiante(int id, String nombre, int edad, TipoSexo sexo, int grado, String uniforme) {
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
        this.grado = grado;
        this.uniforme = uniforme;
    }

    public Estudiante() {
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

    public int getEdad() {
        return edad;
    }

    public void setEdad(byte edad) {
        this.edad = edad;
    }

    public TipoSexo getSexo() {
        return sexo;
    }

    public void setSexo(TipoSexo sexo) {
        this.sexo = sexo;
    }

    public int getGrado() {
        return grado;
    }

    public void setGrado(byte grado) {
        this.grado = grado;
    }

    public String getUniforme() {
        return uniforme;
    }

    public void setUniforme(String uniforme) {
        this.uniforme = uniforme;
    }

    @Override
    public String toString() {
        return "Estudiante{" + "id=" + id + ", nombre=" + nombre + ", edad=" + edad + ", sexo=" + sexo + ", grado=" + grado + ", uniforme=" + uniforme + '}';
    }
}
