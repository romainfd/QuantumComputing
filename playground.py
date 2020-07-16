from qiskit.circuit.library import HGate

from qiskit.aqua.operators import MatrixOp, ComposedOp, SummedOp, X, Z, I, OperatorStateFn, PrimitiveOp, OperatorBase

if __name__ == '__main__':
    assert "\t\tString\n\t\tto indent\n" == OperatorBase.indent("String\nto indent\n", indentation="\t\t")

    print(
        ComposedOp([
            SummedOp([
                ComposedOp([
                    OperatorStateFn(
                        SummedOp(
                            [0.18093119978423136 * Z,
                             -1.052373245772859 * I
                             ],
                            abelian=True
                        ),
                        is_measurement=True
                    ),
                    PrimitiveOp(HGate())
                ]),
                ComposedOp([
                    OperatorStateFn(SummedOp(
                            [0.18093119978423136 * Z,
                             -1.052373245772859 * I
                             - 1.052373245772859 * I
                             ],
                            abelian=True
                        ),
                        is_measurement=True
                    ),
                    I
                ])
            ]),
            PrimitiveOp(HGate())
        ])
    )

    print(ComposedOp([SummedOp([X, Z])]))

    # https://github.com/Qiskit/qiskit-aqua/pull/1111 -> Matrix multiplicative factor (z + z == 2 * z)
    z = MatrixOp([[1, 0], [0, -1]])
    a = Z + z
    b = z + Z
    print(a == b)

    op = MatrixOp([[1, 0], [0, 0]])
    a = 2 * op
    b = op + op
    print((2 * op) == (op + op))
    print(op == op)
    print(2 * X == X + X)
    print(3 * X == X + X + X)
