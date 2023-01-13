/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package com.example.HelloSpring.dao;

import com.example.HelloSpring.domain.Persona;
import org.springframework.data.repository.CrudRepository;

/**
 *
 * @author Usuario
 */
public interface IPersonaDao extends CrudRepository<Persona, Long> {
    
}
