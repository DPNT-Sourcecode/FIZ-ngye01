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
        assert fizz_buzz_solution.fizz_buzz(50) == "buzz"


    def test_15_is_fizz_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(15) == "fizz buzz"

    def test_30_is_fizz_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(30) == "fizz buzz"

    def test_53_is_fizz_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(53) == "fizz buzz"


    def test_11_is_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(11) == "deluxe"


    def test_222_is_fizz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(222) == "fizz deluxe"

    # there are no longer numbers that can be buzz deluxe

    def test_5555_is_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(5555) == "buzz fake deluxe"

    def test_555_is_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(555) == "fizz buzz deluxe"


    def test_2(self):
        assert fizz_buzz_solution.fizz_buzz(2) == "2"

    def test_7(self):
        assert fizz_buzz_solution.fizz_buzz(7) == "7"