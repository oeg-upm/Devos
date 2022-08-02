from ogister.gister import get_matched_keywords_per_text, split_text, get_matched_keywords

import unittest


class TestGister(unittest.TestCase):

    def setUp(self) -> None:
        self.s1 = "This is keyword this is another, and this one, and lastly this."
        self.s2 = "One.Two.Three"
        self.s1_kw = ["This is keyword", "this is another", "and this one", "and lastly this"]
        self.s2_kw = ["One Two Three"]

    def test_matched_keywords_per_text(self):
        keywords = get_matched_keywords_per_text(self.s1, 3, None)
        self.assertEqual(4, len(keywords))
        self.assertEqual(keywords[0], "This is keyword")
        self.assertListEqual(keywords, self.s1_kw)

    def test_split_text(self):
        tokens = ["This", "is", "keyword", "this", "is", "another", "and", "this", "one", "and", "lastly", "this"]
        toks = split_text(self.s1)
        self.assertListEqual(tokens, toks)

    def test_matched_keywords_meta(self):
        keywords = get_matched_keywords([self.s1, self.s2], 3, None)
        print(keywords)
        self.assertEqual(5, len(keywords))
        self.assertListEqual(sorted(keywords), sorted(self.s1_kw+self.s2_kw))


if __name__ == '__main__':
    unittest.main()