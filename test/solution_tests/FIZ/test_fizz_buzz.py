from solutions.FIZ import fizz_buzz_solution


class TestFizzBuzz():
    # divisible by 3
    def test_6_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(6) == "fizz"
    # contains 3
    def test_13_is_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(13) == "fizz"

    # contains 3 and divisible by 3 - even
    def test_432_is_fizz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(432) == "fizz deluxe"
    
    # contains 3 and divisible by 3 - odd
    def test_3_is_fizz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz fake deluxe"

    # divisible by 5
    def test_10_is_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(10) == "buzz"

    # contains 5
    def test_52_is_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(52) == "buzz"
    
    # contains 5 and divisible by 5 - even
    def test_50_is_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz deluxe"

    # contains 5 and divisible by 5 - odd
    def test_5_is_buzz_fake_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz fake deluxe"



    def test_3090_is_fizz_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(3090) == "fizz buzz deluxe"

    def test_3015_is_fizz_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(3015) == "fizz buzz fake deluxe"



    def test_2_is_typical(self):
        assert fizz_buzz_solution.fizz_buzz(2) == "2"

    def test_7_is_typical(self):
        assert fizz_buzz_solution.fizz_buzz(7) == "7"

    def test_22_is_typical(self):
        assert fizz_buzz_solution.fizz_buzz(22) == "22"




