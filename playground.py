from qiskit.circuit.library import HGate

from qiskit.aqua.operators import MatrixOp, ComposedOp, SummedOp, X, Z, I, OperatorStateFn, PrimitiveOp, ListOp

if __name__ == '__main__':
    op = MatrixOp([[1, 0], [0, -1]])
    initial_str = str(op)
    indented_str = op._indent(initial_str)
    starts_with_indent = indented_str.startswith(op.INDENTATION)
    assert starts_with_indent
    indented_str_content = (indented_str[len(op.INDENTATION):] + op.INDENTATION).split("\n{}".format(op.INDENTATION))
    print(indented_str)
    print(initial_str)
    print(indented_str_content)
    print(initial_str.split("\n"))
    assert indented_str_content == initial_str.split("\n")

    assert "\t\tString\n\t\tto indent\n" == ListOp._indent("String\nto indent\n", indentation="\t\t")

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
