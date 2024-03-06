from unittest import TestCase

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_general1(self):
        self.assertEqual(solution(1,9), 8)
    def test_general2(self):
         self.assertEqual(solution(4,17), 12)
    def test_begative_nums(self):
        self.assertEqual(solution(-17, -4), 12)