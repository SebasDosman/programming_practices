/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.HelloSpring;

import com.example.HelloSpring.domain.Persona;
import java.util.ArrayList;
import java.util.Arrays;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
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
    
//    Decorador para renderizar una variable por medio del aplicattion.properties
    @Value("${index.saludo}")
    private String saludo;
    
//    Decorador para servidor por medio de una ruta
    @GetMapping("/")
    public String inicio(Model model) {
       var saludar = "Hello world with Thymeleaf";
       
//       Instancia de la clase persona
       var persona = new Persona();
       
//       Setter de la clase Persona
       persona.setNombre("Juan");
       persona.setApellido("Dosman");
       persona.setEmail("jsdosman0@gmail.com");
       persona.setTelefono("3174515474");
       
//        Instancia de la clase persona
       var persona1 = new Persona();
       
//       Setter de la clase Persona
       persona1.setNombre("Carlos");
       persona1.setApellido("Marquez");
       persona1.setEmail("name@example.com");
       persona1.setTelefono("316268518");
       
//       Declaracion de ArrayList para agregar las personas instanciadas 
//       var personas = new ArrayList<Persona>();
//       personas.add(persona);
//       personas.add(persona1);

//      Reduccion de codigo para declarar y rellenar un ArrayList
        var personas = Arrays.asList(persona, persona1);
       
//       Mensaje a la hora del levantamiento del Localhost
       log.info("Ejecutando el controlador Spring MVC");
       
//       Metodos para agregar al modelo las variables declaradas anteriormente
       model.addAttribute("saludar", saludar);
       model.addAttribute("saludo", saludo);
       model.addAttribute("personas", personas);
       
       
//       Nombre del index.html a mostrar
       return "index";
    }
    
}
