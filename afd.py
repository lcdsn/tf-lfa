class AFD:
    def __init__(
        self,
        name: str,
        alphabet: list,
        states: list,
        transitionTab: dict,
        initState: str,
        finalStates: set,
    ):
        self.name = name
        self.alphabet = alphabet
        self.states = states
        self.transitionTab = transitionTab
        self.initState = initState
        self.finalStates = finalStates

    def getTransition(self, name: str, ch: str):
        if name not in self.states:
            return None

        try:
            return self.transitionTab[name][ch]
        except KeyError:
            return None

    def run(self, word: str):
        cur = self.initState  # estado atual

        for ch in word:
            cur = self.getTransition(cur, ch)
            if cur is None:
                return False

        return True if cur in self.finalStates else False

    def salvaAFD(self, fn: str):
        with open(fn, "w") as f:
            f.write(f"{self.name}=")
            f.write("(")
            f.write("{" + ",".join(self.states) + "},")
            f.write("{" + ",".join(self.alphabet) + "},")
            f.write(f"{self.initState},")
            f.write("{" + ",".join(self.finalStates) + "}")
            f.write(")\n")
            f.write("Prog:\n")

            for e1 in self.transitionTab:
                for e2 in self.transitionTab[e1]:
                    f.write(f"({e1},{e2})={{{self.transitionTab[e1][e2]}}}\n")


if __name__ == "__main__":
    tst = AFD(
        "teste",
        ["a", "b"],  # alfabeto
        ["q0", "q1"],  # estados
        {"q0": {"a": "q1"}, "q1": {"a": "q0"}},  # tabela de transição
        "q0",  # estado inicial
        {"q1"},
    )  # estados finais

    print(tst.run("aaab"))
    print(tst.run("aaa"))
