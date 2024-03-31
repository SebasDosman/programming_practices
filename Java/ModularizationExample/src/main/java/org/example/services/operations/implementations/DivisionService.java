package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.IDivisionService;

public class DivisionService implements IDivisionService {
    @Override
    public int division(int a, int b) {
        return a / b;
    }
}
