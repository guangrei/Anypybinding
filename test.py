# -*- coding: utf-8 -*-
from anybinding import Bind
import json
import unittest


class BindTest(unittest.TestCase):

    def test_satu(self):
        testbin = Bind('testbin')
        espektasi = ["--help"]
        output = json.loads(testbin._('--help'))
        self.assertEqual(output, espektasi)

    def test_dua(self):
        testbin = Bind('testbin')
        espektasi = ["Hello-World"]
        output = json.loads(testbin.Hello_World())
        self.assertEqual(output, espektasi)

    def test_tiga(self):
        testbin = Bind('testbin')
        espektasi = ["coba", "yes", "--foo", "bar", "-s", "egg", "--end"]
        output = json.loads(testbin.coba('yes', foo='bar', s='egg', _='--end'))
        self.assertEqual(output, espektasi)


if __name__ == "__main__":
    unittest.main()
