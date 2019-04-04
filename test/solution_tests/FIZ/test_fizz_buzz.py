from solutions.FIZ import fizz_buzz_solution


class TestFizzBuzz():
    def test_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz"

    def test_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz"

    def test_fizz_buzz_for_15(self):
        assert fizz_buzz_solution.fizz_buzz(15) == "fizz buzz"

    def test_fizz_buzz_for_30(self):
        assert fizz_buzz_solution.fizz_buzz(30) == "fizz buzz"
