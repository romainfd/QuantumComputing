from qiskit.aqua.operators import MatrixOp
from qiskit.aqua.operators import X, Z

if __name__ == '__main__':
    op = MatrixOp([[1, 0], [0, 0]])
    a = 2 * op
    b = op + op
    print((2 * op) == (op + op))
    print(op == op)
    print(2 * X == X + X)
    print(3 * X == X + X + X)
