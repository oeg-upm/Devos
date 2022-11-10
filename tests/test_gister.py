import unittest

import rdflib
import os
from ogister.gister import get_matched_per_text, get_matched
from ogister.util import split_text_manual
# from ogister.util import split_text

split_text = split_text_manual


class TestGister(unittest.TestCase):

    def setUp(self) -> None:
        self.s1 = "This is keyword this is another, and this one, and lastly this."
        self.s2 = "One.Two.Three"
        self.s1_kw = ["This is keyword", "this is another", "and this one", "and lastly this"]
        self.s2_kw = ["One Two Three"]

    def test_matched_keywords_per_text(self):
        g = rdflib.Graph()
        ont_path = os.path.join("data", "ieswc", "SEO.owl")
        g.parse(ont_path)
        keywords, matched_classes, matched_properties = get_matched_per_text("Research field ZZZZZZZ", max_num_tok=3,
                                                                             g=g, only_object_property=False)
        self.assertEqual(1, len(keywords))
        self.assertEqual(keywords[0], "Research field")

    def test_split_text(self):
        tokens = ["This", "is", "keyword", "this", "is", "another", "and", "this", "one", "and", "lastly", "this"]
        toks = split_text(self.s1)
        self.assertListEqual(tokens, toks)

    # def test_matched_keywords_meta(self):
    #     keywords = get_matched([self.s1, self.s2], 3, None)
    #     print(keywords)
    #     self.assertEqual(5, len(keywords))
    #     self.assertListEqual(sorted(keywords), sorted(self.s1_kw+self.s2_kw))


if __name__ == '__main__':
    unittest.main()
