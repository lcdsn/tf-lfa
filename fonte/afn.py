class AFN:
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
        try:
            return self.transitionTab[name][ch]
        except KeyError:
            return set()

    def run(self, word: str, step=False):
        curSet = set([self.initState])  # estado atual

        for i in range(len(word)):
            ch = word[i]
            visited = set()

            while len(curSet):
                state = curSet.pop()
                visited |= self.getTransition(state, ch)

                if step:
                    print(
                        f"index[{i}]='{ch}' current={state} visited={visited}",
                    )

            curSet.update(visited)
            if step:
                print(f"curSet={curSet}")
                input()

        return True if len(curSet & self.finalStates) else False


if __name__ == "__main__":
    tst3 = AFN(
        name="tst3",
        alphabet=["a", "b"],
        states=["q0", "q1", "q2", "qf"],
        transitionTab={
            "q0": {"a": {"q0", "q1"}, "b": {"q0"}},
            "q1": {"a": {"q2"}},
            "q2": {"a": {"qf"}},
        },
        initState="q0",
        finalStates={"qf"},
    )

    print(tst3.run("abb"))
    print(tst3.run("aaabb"))
    print(tst3.run("aaabbb"))
    print(tst3.run("aaabbbb"))
    print(tst3.run("ababaaa"))
