import unittest

import rdflib
import os
from ogister.gister import get_freq_classes, shorten_uris, meta_workflow
from ogister.util import split_text_manual

# from ogister.util import split_text

split_text = split_text_manual


class TestGisterMeta(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_meta_title(self):
        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)

        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "foot ball")
        self.assertEqual(2, len(relations))

    def test_meta_rtop(self):
        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True, topr=1,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)
        print("classes: ")
        print(classes)
        print("relations: ")
        print(relations)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "foot ball")
        self.assertEqual(1, len(relations))


if __name__ == '__main__':
    unittest.main()
