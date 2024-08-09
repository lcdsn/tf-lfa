from unittest import TestCase, main
from afn import AFN


class TestAFN(TestCase):
    def test3(self):
        af = AFN(
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

        assert af.run("abb") == False
        assert af.run("aaabb") == False
        assert af.run("aaabbb") == False
        assert af.run("aaabbbb") == False
        assert af.run("aaa") == True


if __name__ == "__main__":
    main()
