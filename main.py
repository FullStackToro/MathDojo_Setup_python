import unittest
class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result += a
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for a in nums:
            self.result -= a
        return self

#Casos de Prueba
class addTest(unittest.TestCase):

    #setUp se ejecuta cada vez que se realizará una prueba
    def setUp(self):
        self.mdd = MathDojo()

    def test_one(self):
        self.assertEqual(self.mdd.add(6).result, 6)

    def test_two(self):
        self.assertEqual(self.mdd.add(6,8,9,2).result, 25)

    def test_three(self):
        self.assertEqual(self.mdd.add(6).add(12).result, 18)

    def test_four(self):
        self.assertEqual(self.mdd.add(6).add(10,11,12,13,20).subtract(10,11,12,20).result, 19)

    def test_five(self):
        self.assertEqual(self.mdd.add(100).subtract(10,13,12,5).subtract(10,13,17,20).result, 0)


if __name__ == '__main__':
    unittest.main()
else:
    # crear una instruccion:
    md = MathDojo()
    md2 = MathDojo()
    md3 = MathDojo()
    # para probar:
    x3 = md3.add(2).add(2, 5, 1).add(3, 2).result  # 15
    x2 = md2.add(30).subtract(2, 5, 1).subtract(3, 2).subtract(4).result  # 13
    x1 = md.add(2).add(2, 5, 1).subtract(3, 2).result
    print(x1, x2, x3)  # debe imprimir 5
    # corre cada uno de los metodos algunos mas veces y valida el resultado!


