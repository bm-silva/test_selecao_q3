#Input = [1, 7, 13, 22, 5, 12, 30]
Input = [7, 3, 9, 9, 12, 40, 5]


def buscar(Input):
    Output = []
    numeros_desejados = [5, 7, 9]
    for numero in numeros_desejados:
        if numero in Input:
            Output.append(numero)
    return Output


if __name__ == "__main__":
    print(buscar(Input))
