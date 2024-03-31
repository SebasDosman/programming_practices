package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.ISquareRootService;

public class SquareRootService implements ISquareRootService {
    @Override
    public double squareRoot(double a) {
        return Math.sqrt(a);
    }
}
