import unittest

#help(unittest)

import unittest



class IntegerArithmeticTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("打开浏览器")

    @classmethod
    def tearDownClass(cls) -> None:
        print("关闭浏览器")

    #
    # def setUp(self):
    #     print("打开浏览器")
    #
    # def tearDown(self):
    #     print("关闭浏览器")





    def testAdd(self):  # test method names begin with 'test'
        print("1111111")
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        print("2222222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()