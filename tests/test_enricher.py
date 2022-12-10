import unittest

import rdflib
import os
from devos.gister import get_freq_classes, shorten_uris
from devos.util import split_text_manual
# from ogister.util import split_text
from devos.enricher import class_name_to_label

split_text = split_text_manual


class TestEnricher(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_class_name_to_label(self):
        class_name = "One"
        label = "One"
        self.assertEqual(class_name_to_label(class_name), label)

        class_name = "OneTwo"
        label = "One Two"
        self.assertEqual(class_name_to_label(class_name), label)

        class_name = "OneT"
        label = "One T"
        self.assertEqual(class_name_to_label(class_name), label)

        class_name = "OT"
        label = "OT"
        self.assertEqual(class_name_to_label(class_name), label)

        class_name = "USA"
        label = "USA"
        self.assertEqual(class_name_to_label(class_name), label)

        class_name = "UsA"
        label = "Us A"
        self.assertEqual(class_name_to_label(class_name), label)

        class_name = "IPAddress"
        label = "IP Address"
        self.assertEqual(class_name_to_label(class_name), label)


if __name__ == '__main__':
    unittest.main()
