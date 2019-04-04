from solutions.FIZ import fizz_buzz_solution


class TestFizzBuzz():
    def test_3_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz"

    def test_13_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(13) == "fizz"

    def test_3091_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(3091) == "fizz"

    def test_5_is_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz"

    def test_50_is_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz"

    def test_fizz_buzz_for_15(self):
        assert fizz_buzz_solution.fizz_buzz(15) == "fizz buzz"

    def test_fizz_buzz_for_30(self):
        assert fizz_buzz_solution.fizz_buzz(30) == "fizz buzz"

    def test_2(self):
        assert fizz_buzz_solution.fizz_buzz(2) == "2"

    def test_7(self):
        assert fizz_buzz_solution.fizz_buzz(7) == "7"

