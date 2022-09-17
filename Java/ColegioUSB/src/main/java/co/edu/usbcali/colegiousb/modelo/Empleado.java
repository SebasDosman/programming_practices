/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.edu.usbcali.colegiousb.modelo;

import co.edu.usbcali.colegiousb.tipoenum.TipoSexo;
import co.edu.usbcali.colegiousb.tipoenum.TipoRol;
/**
 *
 * @author joseph
 */
public class Empleado {
    private int id;
    private String nombre;
    private int edad;
    private TipoSexo sexo;
    private TipoRol rol;
    private int salario;

    public Empleado(int id, String nombre, int edad, TipoSexo sexo, TipoRol rol, int salario) {
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
        this.rol = rol;
        this.salario = salario;
    }

    public Empleado() {
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

    public TipoRol getRol() {
        return rol;
    }

    public void setRol(TipoRol rol) {
        this.rol = rol;
    }

    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Empleado{" + "id=" + id + ", nombre=" + nombre + ", edad=" + edad + ", sexo=" + sexo + ", rol=" + rol + ", salario=" + salario + '}';
    }
}
