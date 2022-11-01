/**
 * 
 */
package co.edu.usbcali.elxproyecto.repositorio;

import java.io.FileWriter;

import co.edu.usbcali.elxproyecto.modelo.Estudiante;

/**
 * @author salas
 *
 */
public class EstudianteRepositorio implements IEstudianteRepositorio {

	@Override
	public String crearEstudiante(Estudiante estudiante) {

		String cadena = "Se ha creado el estudiante";
		return cadena;
	}

}
