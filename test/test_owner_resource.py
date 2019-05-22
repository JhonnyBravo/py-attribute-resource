# -*- coding: utf-8 -*-
import ConfigParser
import unittest

from py_attribute_resource.py_owner_resource import OwnerResource
from py_directory_resource import DirectoryResource
from py_file_resource import FileResource


class TestFileOwner(unittest.TestCase):
    """
    Tests for OwnerResource class.
    """

    def setUp(self):
        config = ConfigParser.RawConfigParser()
        config.read("test/resources/test.config")
        self.owner = config.get("OwnerResource", "Owner")

        self.resource = OwnerResource("test.txt")
        self.fr = FileResource("test.txt")
        self.fr.create()

    def tearDown(self):
        self.fr.delete()

    def test1(self):
        """
        * Can change file owner.
        * Exit code equals 2 if owner was changed.
        * Exit code equals 0 if owner was not changed.

        * Can get current file owner.
        * Exit code equals 2.
        """
        self.resource.set_owner(self.owner)
        self.assertEqual(2, self.resource.code)

        self.resource.set_owner(self.owner)
        self.assertEqual(0, self.resource.code)

        cur_owner = self.resource.get_owner()
        self.assertEqual(2, self.resource.code)
        self.assertEqual(self.owner, cur_owner)


class TestDirectoryOwner(unittest.TestCase):
    def setUp(self):
        config = ConfigParser.RawConfigParser()
        config.read("test/resources/test.config")
        self.owner = config.get("OwnerResource", "Owner")

        self.resource = OwnerResource("test_dir")
        self.dr = DirectoryResource("test_dir")
        self.dr.create()

    def tearDown(self):
        self.dr.delete()

    def test1(self):
        """
        * Can change directory owner.
        * Exit code equals 2 if owner was changed.
        * Exit code equals 0 if owner was not changed.

        * Can get current directory owner.
        * Exit code equals 2.
        """
        self.resource.set_owner(self.owner)
        self.assertEqual(2, self.resource.code)

        self.resource.set_owner(self.owner)
        self.assertEqual(0, self.resource.code)

        cur_owner = self.resource.get_owner()
        self.assertEqual(2, self.resource.code)
        self.assertEqual(self.owner, cur_owner)


if __name__ == "__main__":
    unittest.main()
