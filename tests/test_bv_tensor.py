import unittest

from syft.he.bv import KeyPair, BVTensor
import numpy as np
from syft import TensorBase


class addition_test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(addition_test, self).__init__(*args, **kwargs)
        self.keys = KeyPair()
        self.keys.generate()

    def test_add(self):
        a = BVTensor(self.keys.pk(), np.asarray([40,2]), True)
        b = a + 2.0
        # TODO decrypt, check plaintext result


class multiplication_test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(multiplication_test, self).__init__(*args, **kwargs)
        self.keys = KeyPair()
        self.keys.generate()

    def test_mul_by_scalarinv(self):
        a = BVTensor(self.keys.pk(), np.asarray([21]), True)
        b = a * 2
        # TODO decrypt, check plaintext result

if __name__ == "__main__":
    unittest.main()
