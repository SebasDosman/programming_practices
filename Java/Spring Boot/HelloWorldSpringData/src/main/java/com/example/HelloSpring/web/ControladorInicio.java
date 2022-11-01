/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.HelloSpring.web;

import com.example.HelloSpring.dao.IPersonaDao;
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
    private IPersonaDao IPersonaDao;
    
//    Decorador para servidor por medio de una ruta
    @GetMapping("/")
    public String inicio(Model model) {       
       var personas = IPersonaDao.findAll();
       
//       Mensaje a la hora del levantamiento del Localhost
       log.info("Ejecutando el controlador Spring MVC");
       
       model.addAttribute("personas", personas);
       
//       Nombre del index.html a mostrar
       return "index";
    }
    
}
