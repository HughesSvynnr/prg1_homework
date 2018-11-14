class Irrational:

    def __init__(self,iterations):
        self.iterations=iterations
        pass


    def _factorial(self,n):
    
        if n < 1:
            return 1
        else:
            return n * self._factorial(n-1)

    def pi(self,accuracy=10000):
        pi=0
        for i in range(1,accuracy):
            pi += ((4.0 * (-1)**i)/(2*i-1))
        return pi * -1

    def e(self,places):
        e = 0
        for number in range(0,places):
            e = e + 1/self._factorial(number)
        return e
not_rational = Irrational(100)

print(not_rational.e(100))

print("`````````")
print(not_rational._factorial(4))
print("`````````")

print(not_rational.pi(100000000000))