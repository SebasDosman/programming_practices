package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.ILogarithmService;

public class LogarithmService implements ILogarithmService {
    @Override
    public double logarithm(double a, double b) {
        return Math.log(a) / Math.log(b);
    }
}
