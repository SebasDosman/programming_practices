package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.ISubtractionService;

public class SubtractionService implements ISubtractionService {
    @Override
    public int subtraction(int a, int b) {
        return a - b;
    }
}
