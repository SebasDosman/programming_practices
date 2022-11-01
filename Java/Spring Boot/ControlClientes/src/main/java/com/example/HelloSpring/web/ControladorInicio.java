/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.HelloSpring.web;

import com.example.HelloSpring.servicio.PersonaService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
/**
 *
 * @author Usuario
 */
@Controller
@Slf4j
public class ControladorInicio {
    @Autowired
    private PersonaService personaService;
    
    @GetMapping("/")
    public String inicio(Model model) {       
       var personas = personaService.listarPersonas();
       log.info("Ejecutando el controlador Spring MVC");
       model.addAttribute("personas", personas);
       return "index";
    }
    
}
