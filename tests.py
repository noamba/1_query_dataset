import unittest
from search_app_base import calculate_score 

class SearchTestCase(unittest.TestCase):

    def test_score_is_1_on_perfect_match(self):
        query = "Red Shirt Prada"
        entry= [1234,"Red Shirt","Prada"]

        self.assertEqual(_get_score(query, entry), 1)

    def test_score_is_1_on_perfect_match_with_repetition(self):
        query = "Red Shirt Prada"
        entry= [1234,"Red Shirt Prada Red","Prada"]

        self.assertEqual(_get_score(query, entry), 1)

    def test_score_is_between_0_and_1_on_partial_match(self):
        query = "Red Trousers"
        entry= [1234,"Red Shirt Prada","Prada"]

        self.assertTrue(0 < _get_score(query, entry) < 1)


def _get_score(query,entry):
        
    keywords = query.split()
    return(calculate_score(keywords, entry))

if __name__ == "__main__":
    unittest.main()
