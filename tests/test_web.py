import unittest

import rdflib
import os
from devos.gister import get_freq_classes, shorten_uris, meta_workflow
from devos.util import split_text_manual
from web.app import app
from werkzeug.datastructures import FileStorage




class TestGisterMeta(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_home_get(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_post_file(self):
        client = app.test_client()
        ont_path = os.path.join("data", "ieswc", "quotekg_schema.ttl")

        my_file = FileStorage(
            stream=open(ont_path, "rb"),
            filename="ont.ttl")

        data = {'file': my_file}
        response = client.post('/', data=data, content_type='multipart/form-data')
        self.assertEquals(response.status_code, 200)

    def test_home_post_url(self):
        client = app.test_client()
        url = 'https://raw.githubusercontent.com/oeg-upm/morph-rdb/master/morph-examples/examples-csv/SPORT.csv'
        data = {'url': url}
        response = client.post('/', data=data, content_type='multipart/form-data')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
