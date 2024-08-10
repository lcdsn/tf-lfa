class AFD:
    def __init__(
        self,
        alphabet: list,
        states: list,
        transitionTab: dict,
        initState: str,
        finalStates: set,
    ):
        self.alphabet = alphabet
        self.states = states
        self.transitionTab = transitionTab
        self.initState = initState
        self.finalStates = finalStates

    def getTransition(self, name: str, ch: str):
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


if __name__ == "__main__":
    tst = AFD(
        ["a", "b"],  # alfabeto
        ["q0", "q1"],  # estados
        {"q0": {"a": "q1"}, "q1": {"a": "q0"}},  # tabela de transição
        "q0",  # estado inicial
        {"q1"},
    )  # estados finais

    print(tst.run("aaab"))
    print(tst.run("aaa"))
