import unittest

import rdflib
import os
from ogister.gister import get_freq_classes, shorten_uris, meta_workflow
from ogister.util import split_text_manual

split_text = split_text_manual


class TestGisterMeta(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_meta_title_soft(self):
        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True, soft=True,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "foot ball")
        self.assertEqual(2, len(relations))

    def test_meta_title_hard(self):
        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True, soft=False,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)

        self.assertEqual(2, len(classes))
        self.assertEqual(classes[0], "foot ball")
        self.assertEqual(2, len(relations))

    def test_meta_rtop_soft(self):
        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True, topr=1, soft=True,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "foot ball")
        self.assertEqual(1, len(relations))

    def test_meta_rtop_hard_topn1(self):
        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True, topr=1, topn=1,
                                           soft=False,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "foot ball")
        self.assertEqual(1, len(relations))

    def test_meta_rtop_hard_topn0(self):
        ont_path = os.path.join("tests", "o2.ttl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True, topn=1,
                                           soft=False,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)
        self.assertEqual(1, len(classes))
        self.assertEqual(classes[0], "foot ball")
        # self.assertEqual(1, len(relations))

    def test_meta_explanation_top7(self):
        ont_path = os.path.join("data", "ieswc_enriched", "explanation-ontology.owl")
        classes, relations = meta_workflow(input_path=ont_path, title=True, desc=True, abstract=True, topn=7,
                                           soft=False,
                                           only_object_property=True, out_path=None, lang=None, max_options=0)
        self.assertEqual(7, len(classes))
        from_classes = [r[0] for r in relations]
        to_classes = [r[2] for r in relations]
        rclasses = list(set(from_classes+to_classes))
        self.assertLessEqual(len(rclasses), 7)


if __name__ == '__main__':
    unittest.main()
