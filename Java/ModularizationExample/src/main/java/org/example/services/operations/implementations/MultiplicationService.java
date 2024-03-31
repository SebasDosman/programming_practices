package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.IMultiplicationService;

public class MultiplicationService implements IMultiplicationService {
    @Override
    public int multiplication(int a, int b) {
        return a * b;
    }
}
