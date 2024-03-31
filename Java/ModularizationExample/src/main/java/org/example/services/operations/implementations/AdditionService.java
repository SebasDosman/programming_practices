package org.example.services.operations.implementations;

import org.example.services.operations.interfaces.IAdditionService;

public class AdditionService implements IAdditionService {
    @Override
    public int addition(int a, int b) {
        return a + b;
    }
}
