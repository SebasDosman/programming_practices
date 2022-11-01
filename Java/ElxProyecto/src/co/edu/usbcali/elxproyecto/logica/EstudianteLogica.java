/**
 * 
 */
package co.edu.usbcali.elxproyecto.logica;

import co.edu.usbcali.elxproyecto.modelo.Estudiante;
import co.edu.usbcali.elxproyecto.repositorio.IEstudianteRepositorio;

/**
 * @author salas
 *
 */
public class EstudianteLogica implements IEstudianteLogica{

	private IEstudianteRepositorio estudianteRepositorio;
	
	@Override
	public String crearEstudiante(Estudiante estudiante) {
		String cadena = estudianteRepositorio.crearEstudiante(estudiante);

		return cadena;
	}

}
