import unittest
from search import search

class SearchTests(unittest.TestCase):
    def test_matching_course(self):
        self.assertEqual(len(search("智能化")), 2)
    def test_no_results(self):
        self.assertEqual(search("不存在的课程"), [])

if __name__ == "__main__":
    unittest.main()
