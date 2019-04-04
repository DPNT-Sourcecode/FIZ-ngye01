from solutions.FIZ import fizz_buzz_solution


class TestFizzBuzz():
    # divisible by 3
    def test_6_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(6) == "fizz"
    # contains 3
    def test_13_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(13) == "fizz"
    
    # contains 3 and divisible by 3
    def test_3_is_fizz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz deluxe"

    def test_3090_is_fizz_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(3090) == "fizz buzz deluxe"


    # divisible by 3
    def test_10_is_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(6) == "fizz"
    # contains 3
    def test_13_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(13) == "fizz"
    
    # contains 3 and divisible by 3
    def test_3_is_fizz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz deluxe"

    def test_3090_is_fizz_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(3090) == "fizz buzz deluxe"


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

    # def test_333_is_fizz_fake_deluxe(self):
    #     assert fizz_buzz_solution.fizz_buzz(333) == "fizz fake deluxe"

    # # there are no longer numbers that can be buzz deluxe

    # def test_5555_is_buzz_fake_deluxe(self):
    #     assert fizz_buzz_solution.fizz_buzz(5555) == "buzz fake deluxe"

    # def test_555_is_fizz_buzz_fake_deluxe(self):
    #     assert fizz_buzz_solution.fizz_buzz(555) == "fizz buzz fake deluxe"


    def test_2_is_typical(self):
        assert fizz_buzz_solution.fizz_buzz(2) == "2"

    def test_7_is_typical(self):
        assert fizz_buzz_solution.fizz_buzz(7) == "7"

    def test_22_is_typical(self):
        assert fizz_buzz_solution.fizz_buzz(22) == "22"


