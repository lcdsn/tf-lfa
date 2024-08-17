from afn import AFN
from afd import AFD

from collections import deque


def convert(afn: AFN):
    newStates = {}
    queue = deque([afn.initState])
    newTable = dict()

    for states in afn.states:
        newStates[states] = {states}

    while queue:
        curState = queue.popleft()

        for ch in afn.alphabet:
            s = set()
            for state in newStates[curState]:
                try:
                    s = s.union(afn.transitionTab[state][ch])
                except KeyError:
                    continue

            newState = "".join(sorted(s))

            if len(newState):
                if newState not in newTable:
                    if newState not in newStates:
                        newStates[newState] = s
                    queue.append(newState)

                newTable.setdefault(curState, {}).update({ch: newState})

    finalStates = set()
    for state in newTable:
        if len(newStates[state] & afn.finalStates):
            finalStates = finalStates.union([state])

    return AFD(
        name=afn.name + "_AFD",
        alphabet=afn.alphabet,
        states=list(newTable.keys()),
        transitionTab=newTable,
        initState=afn.initState,
        finalStates=finalStates,
    )


def main():
    afn = AFN(
        "teste",
        ["a", "b"],  # alfabeto
        ["q0", "q1", "q2", "qf"],  # estados
        {
            "q0": {"a": {"q1", "q0"}, "b": {"q0"}},
            "q1": {"a": {"q2"}},
            "q2": {"a": {"qf"}},
        },  # tabela de transição
        "q0",  # estado inicial
        {"qf"},  # estados finais
    )
    afd = convert(afn)
    print(afd.run("aaa"))
    print(afd.run("baaa"))
    print(afd.run("aba"))


if __name__ == "__main__":
    main()
