import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) throws Exception {
        String s1 = "", s2 = "", nom1 = "", nom2 = "";
        int opcion = 0;
        
        nom1 = JOptionPane.showInputDialog(null, "Digite su nombre jugador 1", "Piedra, Papel o Tijera", JOptionPane.INFORMATION_MESSAGE);
        nom2 = JOptionPane.showInputDialog(null, "Digite su nombre jugador 2", "Piedra, Papel o Tijera", JOptionPane.INFORMATION_MESSAGE);

        do {
            s1 = JOptionPane.showInputDialog(null, nom1 + " digite su opción", "Piedra, Papel o Tijera", JOptionPane.QUESTION_MESSAGE);
            s2 = JOptionPane.showInputDialog(null, nom2 + " digite su opción", "Piedra, Papel o Tijera", JOptionPane.QUESTION_MESSAGE);

            if (s1.equals("piedra") && s2.equals("papel")) {
                JOptionPane.showMessageDialog(null, "¡" + nom2 + " has ganado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
            } else {
                if (s1.equals("papel") && s2.equals("piedra")) {
                    JOptionPane.showMessageDialog(null, "¡" + nom1 + " has ganado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                } else {
                    if (s1.equals("papel") && s2.equals("tijera")) {
                        JOptionPane.showMessageDialog(null, "¡" + nom2 + " has ganado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                    } else {
                        if (s1.equals("tijera") && s2.equals("papel")) {
                            JOptionPane.showMessageDialog(null, "¡" + nom1 + " has ganado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                        } else {
                            if (s1.equals("tijera") && s2.equals("piedra")) {
                                JOptionPane.showMessageDialog(null, "¡" + nom2 + " has ganado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                            } else {
                                if (s1.equals("piedra") && s2.equals("tijera")) {
                                    JOptionPane.showMessageDialog(null, "¡" + nom1 + " has ganado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                                } else {
                                    if (s1.equals("tijera") && s2.equals("tijera")) {
                                        JOptionPane.showMessageDialog(null, "¡Han empatado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                                    } else {
                                        if (s1.equals("piedra") && s2.equals("piedra")) {
                                            JOptionPane.showMessageDialog(null, "¡Han empatado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                                        } else {
                                            if (s1.equals("papel") && s2.equals("papel")) {
                                                JOptionPane.showMessageDialog(null, "¡Han empatado!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            
            opcion = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite: \n 1. Si desea terminar la partida \n 2. Si desea continuar", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE));

            if (opcion == 1) {
                JOptionPane.showMessageDialog(null, "¡Muchas gracias por jugar!", "Piedra, Papel o Tijera", JOptionPane.WARNING_MESSAGE);
            }
        } while (opcion != 1);
    }
}
