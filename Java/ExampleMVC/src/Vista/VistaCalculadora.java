package Vista;

import Controlador.ControladorCalculadora;

//Una interface para los metodos que se van a utilizar en la GUI
public interface VistaCalculadora {
    public int setNumero1(int num1);
    public int setNumero2(int num2);
    public void setResultado(String resultado);
    public void iniciar(ControladorCalculadora controlador);
}
