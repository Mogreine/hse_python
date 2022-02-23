import numpy as np

from hw3.matrix import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    a_np = np.random.randint(0, 10, (10, 10))
    b_np = np.random.randint(0, 10, (10, 10))

    a = Matrix(a_np)
    b = Matrix(b_np)

    (a + b).save("./artifacts/medium/matrix+.txt")
    (a * b).save("./artifacts/medium/matrix*.txt")
    (a @ b).save("./artifacts/medium/matrix@.txt")
