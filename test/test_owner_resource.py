# -*- coding: utf-8 -*-
import ConfigParser
import platform
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

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test1(self):
        """
        * Can change file owner.
        * Exit code equals 2 if owner was changed.
        * Exit code equals 0 if owner was not changed.

        * Can get current file owner.
        * Exit code equals 2.
        """
        self.resource.set_attribute(self.owner)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(self.owner)
        self.assertEqual(0, self.resource.code)

        cur_owner = self.resource.get_attribute()
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

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test1(self):
        """
        * Can change directory owner.
        * Exit code equals 2 if owner was changed.
        * Exit code equals 0 if owner was not changed.

        * Can get current directory owner.
        * Exit code equals 2.
        """
        self.resource.set_attribute(self.owner)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(self.owner)
        self.assertEqual(0, self.resource.code)

        cur_owner = self.resource.get_attribute()
        self.assertEqual(2, self.resource.code)
        self.assertEqual(self.owner, cur_owner)


class TestWindows(unittest.TestCase):
    """
    Tests for Windows platform.
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

    @unittest.skipIf(platform.system() != "Windows", "Test for Windows.")
    def test1(self):
        """
        Exit code equals 1 if platform equals Windows.
        """
        owner = self.resource.get_attribute()
        self.assertEqual(1, self.resource.code)
        self.assertFalse(owner)

    @unittest.skipIf(platform.system() != "Windows", "Test for Windows.")
    def test2(self):
        """
        Exit code equals 1 if platform equals Windows.
        """
        self.resource.set_attribute(self.owner)
        self.assertEqual(1, self.resource.code)


if __name__ == "__main__":
    unittest.main()
