package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.IPowerService;

public class PowerService implements IPowerService {
    @Override
    public double power(int base, int exponente) {
        return Math.pow(base, exponente);
    }
}
