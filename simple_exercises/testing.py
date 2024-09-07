import unittest
from generator import fibonacci

class TestGenerator(unittest.TestCase):
    def test_fibonacci(self):
        num = 6
        result = fibonacci(num)
        self.assertEqual(list(result),[0,1,1,2,3,5])
    def test_fibonacci2(self):
        num = 6
        num=fibonacci(num)
        with self.assertRaises(TypeError):
            list(fibonacci(num))
    
    
unittest.main()