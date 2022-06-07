import Controlador.ControladorCalculadora;
import Modelo.Calculadora;
import Vista.VistaCalculadoraGUI;

public class App {
    public static void main(String[] args) throws Exception {
        VistaCalculadoraGUI vista = new VistaCalculadoraGUI();
        Calculadora calculadora = new Calculadora();
        ControladorCalculadora controlador = new ControladorCalculadora(vista, calculadora);
        controlador.iniciar();
    }
}
