package org.example.calculator;

import org.example.services.menu.interfaces.IMenuService;
import org.example.services.menu.implementations.MenuService;
import org.example.services.operations.implementations.*;
import org.example.services.operations.interfaces.*;
import org.example.utility.Constants;

import javax.swing.JOptionPane;

public class Calculator {
    public void start() {
        int option, a, b;
        IMenuService menuService = new MenuService();

        while(true) {
            option = menuService.menu();

            switch (option) {
                case 1:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));
                    b = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_SECOND_NUMBER));

                    IAdditionService additionService = new AdditionService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + additionService.addition(a, b), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 2:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));
                    b = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_SECOND_NUMBER));

                    ISubtractionService subtractionService = new SubtractionService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + subtractionService.subtraction(a, b), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 3:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));
                    b = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_SECOND_NUMBER));

                    IMultiplicationService multiplicationService = new MultiplicationService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + multiplicationService.multiplication(a, b), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 4:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));
                    b = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_SECOND_NUMBER));

                    IDivisionService divisionService = new DivisionService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + divisionService.division(a, b), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 5:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));
                    b = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_SECOND_NUMBER));

                    IPowerService powerService = new PowerService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + powerService.power(a, b), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 6:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));

                    ISquareRootService squareRootService = new SquareRootService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + squareRootService.squareRoot(a), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 7:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));
                    b = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_SECOND_NUMBER));

                    IModulusService modulusService = new ModulusService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + modulusService.modulus(a, b), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 8:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));
                    b = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_SECOND_NUMBER));

                    ILogarithmService logarithmService = new LogarithmService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + logarithmService.logarithm(a, b), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 9:
                    a = Integer.parseInt(JOptionPane.showInputDialog(Constants.INPUT_FIRST_NUMBER));

                    IFactorialService factorialService = new FactorialService();
                    JOptionPane.showMessageDialog(null, Constants.RESULT + factorialService.factorial(a), Constants.TITLE, JOptionPane.INFORMATION_MESSAGE);
                    break;
                case 10:
                    JOptionPane.showMessageDialog(null, Constants.GOODBYE, Constants.TITLE, JOptionPane.WARNING_MESSAGE);
                    return;
                default:
                    JOptionPane.showMessageDialog(null, Constants.INVALID_OPTION, Constants.TITLE, JOptionPane.ERROR_MESSAGE);
                    break;
            }
        }
    }
}
