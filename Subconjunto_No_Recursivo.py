from itertools import combinations


def Subconjunto_de_un_conjunto(conjunto, n):
    if n == 0:
        print([["no hay una cantidad de elementos para hacer un subconjunto de m"]])

    if len(conjunto) == 0:
        print([["el conjunto m esta vacio"]])

    for subconjunto_de_m in combinations(conjunto, n):
        print(subconjunto_de_m)


if __name__ == "__main__":
    conjunto_m = ["A", "C", "E", "k"]
    n = 2
    Subconjunto_de_un_conjunto(conjunto_m, n)
