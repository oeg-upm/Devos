import unittest

import rdflib
import os
from ogister.gister import get_freq_classes, shorten_uris
from ogister.util import split_text_manual
# from ogister.util import split_text

split_text = split_text_manual


class TestGisterFreq(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_freq(self):
        g = rdflib.Graph()
        ont_path = os.path.join("tests", "o1.ttl")
        g.parse(ont_path)
        classes = get_freq_classes(g=g, topn=1, only_object_property=True)
        classes = shorten_uris(classes)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "football")


if __name__ == '__main__':
    unittest.main()
