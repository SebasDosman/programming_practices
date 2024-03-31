package org.example.services.menu.implementations;

import org.example.services.menu.interfaces.IMenuService;
import org.example.utility.Constants;

import javax.swing.JOptionPane;

public class MenuService implements IMenuService {
    @Override
    public int menu() {
        return Integer.parseInt(JOptionPane.showInputDialog(null, Constants.INPUT_OPTIONS, Constants.TITLE, JOptionPane.INFORMATION_MESSAGE));
    }
}
