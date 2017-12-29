from unittest import TestCase
from assertpy import assert_that
from src.xor import Xor


class XorTests(TestCase):

    def test_to_binary(self):
        x = Xor(0b1011001, "triangle")
        assert_that(x.text).is_equal_to([0b1110100, 0b1110010, 0b1101001, 0b1100001, 0b1101110,
                                         0b1100111, 0b1101100, 0b1100101])

    def test_encoding(self):
        x = Xor(0b10101010, "hi")
        assert_that(x.encoded).is_equal_to(['11000010', '11000011'])
