import unittest

import rdflib
import os
from devos.gister import get_freq_classes, shorten_uris, get_leng_classes
from devos.util import split_text_manual
from devos.prefixes import DBO
# from ogister.util import split_text

split_text = split_text_manual


class TestGisterLeng(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_leng(self):
        g = rdflib.Graph()
        ont_path = os.path.join("tests", "o3.ttl")
        g.parse(ont_path)

        classes, classes_dict = get_leng_classes(g, 10)
        print(classes_dict)
        classes = shorten_uris(classes)
        self.assertEqual(2, len(classes))
        self.assertEqual(classes_dict[DBO+"football"], 2)
        self.assertEqual(classes_dict[DBO+"basket"], 3)

    def test_leng_top1(self):
        g = rdflib.Graph()
        ont_path = os.path.join("tests", "o3.ttl")
        g.parse(ont_path)

        classes, classes_dict = get_leng_classes(g, 1)
        print(classes_dict)
        # classes = shorten_uris(classes)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes_dict[DBO+"basket"], 3)
        self.assertEqual(classes[0], DBO+"basket")


if __name__ == '__main__':
    unittest.main()
