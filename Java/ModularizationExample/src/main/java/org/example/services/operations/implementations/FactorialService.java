package org.example.services.operations.implementations;

import org.apache.commons.math3.util.CombinatoricsUtils;
import org.example.services.operations.interfaces.IFactorialService;

public class FactorialService implements IFactorialService {
    @Override
    public long factorial(int n) {
        return CombinatoricsUtils.factorial(n);
    }
}
