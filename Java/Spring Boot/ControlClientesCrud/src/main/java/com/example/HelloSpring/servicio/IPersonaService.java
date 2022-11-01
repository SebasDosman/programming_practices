/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.HelloSpring.servicio;

import com.example.HelloSpring.domain.Persona;
import java.util.List;

/**
 *
 * @author Usuario
 */
public interface IPersonaService {
    public List<Persona> listarPersonas();
    public void guardarPersona(Persona persona);
    public void eliminarPersona(Persona persona);
    public Persona encontrarPersona(Persona persona);
}
