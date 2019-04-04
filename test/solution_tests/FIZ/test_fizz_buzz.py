from solutions.FIZ import fizz_buzz_solution


class TestFizzBuzz():
    def test_fizz_buzz(self):
        assert fizz_buzz_solution.fizz_buzz("John") == "fizz_buzz, John!"
        # assert fizz_buzz_solution.fizz_buzz("Alice") == "fizz_buzz, Alice!"

