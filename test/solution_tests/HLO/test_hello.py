from solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello("") == "Hello, World!"
        # assert hello_solution.hello(1, 5) == 6


