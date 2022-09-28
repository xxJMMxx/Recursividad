def Subconjunto_de_un_conjunto(conjunto, n):
    if n == 0:
        return [["no hay una cantidad de elementos para hacer un subconjunto de m"]]

    if len(conjunto) == 0:
        print([["el conjunto m esta vacio"]])

    subconjunto = []
    for i in range(0, len(conjunto)):

        elemento_partida = conjunto[i]
        nuevo_sub = conjunto[i + 1:]

        for x in Subconjunto_de_un_conjunto(nuevo_sub, n - 1):
            subconjunto.append([elemento_partida] + x)

    return subconjunto


if __name__ == "__main__":
    conjunto_m = ["A", "C", "E", "k"]
    n = 2
    print(Subconjunto_de_un_conjunto(conjunto_m, n))
