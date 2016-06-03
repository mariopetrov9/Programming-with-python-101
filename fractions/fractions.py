class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        num1 = self.numerator
        num2 = other.numerator
        denom1 = self.denominator
        denom2 = other.denominator
        return num1 == num2 and denom1 == denom2
        return False

    def __hash__(self):
        return hash(self.numerator)

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction.simplify(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction.simplify(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction.simplify(new_numerator, new_denominator)

    def greater_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(numerator, denominator):
        gcd = Fraction.greater_common_divisor(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        if denominator == 0:
            return "Infinity"
        if numerator == 0:
            return 0
        if numerator == denominator:
            return 1
        if denominator == 1:
            return numerator
        return Fraction(numerator, denominator)

a = Fraction(5, 3)
b = Fraction(5, 3)
print(a * b)
