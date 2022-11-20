from unittest import TestCase

from pe33digitcancelfraction import main


class Test(TestCase):
    def test_main(self):
        self.assertEqual(main(2, 1), (110, 322))
        self.assertEqual(main(3, 1), (77262, 163829))
        self.assertEqual(main(3, 2), (7429, 17305))
        self.assertEqual(main(4, 1), (12999936, 28131911))
        self.assertEqual(main(4, 2), (3571225, 7153900))
        self.assertEqual(main(4, 3), (255983, 467405))

