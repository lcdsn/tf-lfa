import pprint

from afn import AFN


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
        alphabet=alfabeto,
        states=estados,
        transitionTab=tabelaTransicao,
        initState=estadoInicial,
        finalStates=set(estadosFinais),
    )


def main():
    afn = parseFile("automato.txt")
    # pprint.pprint(afn.transitionTab, sort_dicts=False)

    with open("lista_de_palavras.txt", "r") as f:
        for line in f:
            print(line.strip(), afn.run(line.strip()))

    # s = "___JMP_H10;___NOP;___AND_H6E;___JN_H7A;___STA_H8A"
    # print(afn.run(s, step=False))


if __name__ == "__main__":
    main()
