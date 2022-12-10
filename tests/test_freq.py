import unittest

import rdflib
import os
from devos.gister import get_freq_classes, shorten_uris, freq_workflow, get_label
from devos.util import split_text_manual

split_text = split_text_manual


class TestGisterFreq(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_freq(self):
        g = rdflib.Graph()
        ont_path = os.path.join("tests", "o1.ttl")
        g.parse(ont_path)
        classes = get_freq_classes(g=g, topn=1, only_object_property=True)
        self.assertEqual(1, len(classes))
        self.assertEqual(str(get_label(g, classes[0])), "foot ball")

    def test_freq_topn0(self):
        ont_path = os.path.join("tests", "o1.ttl")
        classes, relations = freq_workflow(input_path=ont_path, out_path=None, topn=0, only_object_property=True, topr=0, soft=False)
        self.assertEqual(3, len(classes))
        self.assertEqual(classes[0], "foot ball")
        self.assertEqual(3, len(relations))


if __name__ == '__main__':
    unittest.main()
