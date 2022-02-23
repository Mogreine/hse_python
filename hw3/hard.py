import numpy as np

from hw3.matrix import Matrix

if __name__ == "__main__":
    a = Matrix.from_file("./artifacts/hard/A.txt")
    b = Matrix.from_file("./artifacts/hard/B.txt")
    c = Matrix.from_file("./artifacts/hard/C.txt")
    d = Matrix.from_file("./artifacts/hard/D.txt")

    print(f"hash(A): {a.__hash__()}")
    print(f"hash(C): {c.__hash__()}")

    ab = a @ b
    cd = c @ d
    ab.save("./artifacts/hard/AB.txt")
    Matrix(np.array(d.data) @ np.array(c.data)).save("./artifacts/hard/CD.txt")

    with open("./artifacts/hard/hash.txt", "w") as f:
        f.write(str(ab.__hash__()) + "\n")
        f.write(str(cd.__hash__()) + "\n")
