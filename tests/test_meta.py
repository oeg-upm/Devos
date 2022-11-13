import unittest

import rdflib
import os
from ogister.gister import get_freq_classes, shorten_uris, workflow
from ogister.util import split_text_manual
# from ogister.util import split_text

split_text = split_text_manual


class TestMeta(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_meta_title(self):

        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = workflow(input_path=ont_path, title=True, desc=True, abstract=True, only_object_property=True,
                 out_path=None, lang=None, max_options=0)

        # classes = shorten_uris(classes)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "football")


if __name__ == '__main__':
    unittest.main()
