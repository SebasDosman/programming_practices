package co.edu.usbcali.elxproyecto.modelo;

public class Estudiante {
	private String codigo, nombre, carrera, setso;

	/**
	 * 
	 */
	public Estudiante() {
		super();
	}
	
	/**
	 * @param codigo
	 * @param nombre
	 * @param carrera
	 * @param setso
	 */
	public Estudiante(String codigo, String nombre, String carrera, String setso) {
		super();
		this.codigo = codigo;
		this.nombre = nombre;
		this.carrera = carrera;
		this.setso = setso;
	}


	/**
	 * @return the codigo
	 */
	public String getCodigo() {
		return codigo;
	}

	/**
	 * @param codigo the codigo to set
	 */
	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	/**
	 * @return the nombre
	 */
	public String getNombre() {
		return nombre;
	}

	/**
	 * @param nombre the nombre to set
	 */
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	/**
	 * @return the carrera
	 */
	public String getCarrera() {
		return carrera;
	}

	/**
	 * @param carrera the carrera to set
	 */
	public void setCarrera(String carrera) {
		this.carrera = carrera;
	}

	/**
	 * @return the setso
	 */
	public String getSetso() {
		return setso;
	}

	/**
	 * @param setso the setso to set
	 */
	public void setSetso(String setso) {
		this.setso = setso;
	}


	
	
}
