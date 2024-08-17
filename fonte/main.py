import sys

from pprint import pprint
from afn import AFN
from afd import AFD

from convert import convert


def parseFile(fn: str):
    with open(fn, "r") as f:
        definicao = f.readline().strip()
        nome, definicao = definicao.split("=")

        def parser(text: str, delimiters: list):
            if not len(text):
                return [""] * len(delimiters)

            res = []
            textIndex = 0

            for delim in delimiters:
                delimIndex = 0
                left, right = 0, 0

                while delimIndex < len(delim):
                    # print(delim[delimIndex], text[textIndex], left, right)

                    if delim[delimIndex] == text[textIndex]:
                        if delimIndex == 0:
                            left = textIndex
                        elif delimIndex == len(delim) - 1:
                            right = textIndex
                            break
                        delimIndex += 1
                    textIndex += 1

                res.append(text[left + 1 : right])
            return res

        estados, alfabeto, estadoInicial, estadosFinais = parser(
            definicao, ["{}", "{}", ",,", "{}"]
        )

        estados = estados.split(",")
        alfabeto = alfabeto.split(",")
        estadosFinais = estadosFinais.split(",")

        if f.readline().strip() != "Prog":
            print("Função programa não encontrada.")
            exit()

        tabelaTransicao = {}
        while True:
            line = f.readline().strip()
            if not line:
                break

            estado, transicao, destinos = parser(line, ["(,", ",)", "{}"])
            destinos = destinos.split(",")

            tabelaTransicao.setdefault(estado, {})
            tabelaTransicao[estado].setdefault(transicao, set()).update(destinos)

    return AFN(
        name=nome,
        alphabet=alfabeto,
        states=estados,
        transitionTab=tabelaTransicao,
        initState=estadoInicial,
        finalStates=set(estadosFinais),
    )


def main():
    if len(sys.argv) != 3:
        print("Uso: .\determinizador.exe <automato> <lista-palavras>")
        sys.exit(1)

    afn = parseFile(sys.argv[1])
    afd = convert(afn)
    # pprint(afd.transitionTab, sort_dicts=False)
    # pprint(afd.finalStates)
    # exit()

    with open(sys.argv[2], "r") as f:
        for line in f:
            print(line.strip(), afd.run(line.strip()))

    print()
    while True:
        op = input("Salvar AFD? [Y/N]: ")
        if op.lower() == "y":
            afd.salvaAFD(afd.name + ".txt")
            print(f"Autômato salvo em {afd.name}.txt")
            break
        elif op.lower == "n":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
