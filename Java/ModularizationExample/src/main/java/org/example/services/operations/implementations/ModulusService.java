package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.IModulusService;

public class ModulusService implements IModulusService {
    @Override
    public int modulus(int a, int b) {
        return a % b;
    }
}
