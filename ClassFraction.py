class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d
    
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)
    
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)
    
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)
    
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return Fraction(temp_num, temp_den)

# Get user input for fractions
num1 = int(input("Enter the numerator for fraction 1: "))
den1 = int(input("Enter the denominator for fraction 1: "))
num2 = int(input("Enter the numerator for fraction 2: "))
den2 = int(input("Enter the denominator for fraction 2: "))

# Create instances of Fraction using user input
frac1 = Fraction(num1, den1)
frac2 = Fraction(num2, den2)

# Perform arithmetic operations and print the results
print("Fraction 1:", frac1)
print("Fraction 2:", frac2)
print("Addition:", frac1 + frac2)
print("Subtraction:", frac1 - frac2)
print("Multiplication:", frac1 * frac2)
print("Division:", frac1 / frac2)
