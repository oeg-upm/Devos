import unittest

import rdflib
import os
from devos.gister import get_freq_classes, shorten_uris
from devos.util import split_text_manual
from userstudy import class_analytics as analytics
# from ogister.util import split_text
from devos.enricher import class_name_to_label

split_text = split_text_manual


class TestAnalytics(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_is_blank_node(self):
        n = "n138f2aa1334245249f199a3a32ee6c50b20"
        self.assertTrue(analytics.is_blanknode(n))
        n = "nf38f2aa1334245249f199a3a32ee6c50b20"
        self.assertTrue(analytics.is_blanknode(n))
        n = "k138f2aa1334245249f199a3a32ee6c50b20"
        self.assertFalse(analytics.is_blanknode(n))


if __name__ == '__main__':
    unittest.main()
