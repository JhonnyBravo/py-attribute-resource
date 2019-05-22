# -*- coding: utf-8 -*-
import ConfigParser
import unittest

from py_attribute_resource.py_group_resource import GroupResource
from py_directory_resource import DirectoryResource
from py_file_resource import FileResource


class TestFileGroup(unittest.TestCase):
    """
    Tests for GroupResource class.
    """

    def setUp(self):
        config = ConfigParser.RawConfigParser()
        config.read("test/resources/test.config")
        self.group = config.get("GroupResource", "Group")

        self.resource = GroupResource("test.txt")
        self.fr = FileResource("test.txt")
        self.fr.create()

    def tearDown(self):
        self.fr.delete()

    def test1(self):
        """
        * Can change file group owner.
        * Exit code equals 2 if group owner was changed.
        * Exit code equals 0 if group owner was not changed.

        * Can get current file group owner.
        * Exit code equals 2.
        """
        self.resource.set_group(self.group)
        self.assertEqual(2, self.resource.code)

        self.resource.set_group(self.group)
        self.assertEqual(0, self.resource.code)

        cur_owner = self.resource.get_group()
        self.assertEqual(2, self.resource.code)
        self.assertEqual(self.group, cur_owner)


class TestDirectoryGroup(unittest.TestCase):
    def setUp(self):
        config = ConfigParser.RawConfigParser()
        config.read("test/resources/test.config")
        self.group = config.get("GroupResource", "Group")

        self.resource = GroupResource("test_dir")
        self.dr = DirectoryResource("test_dir")
        self.dr.create()

    def tearDown(self):
        self.dr.delete()

    def test1(self):
        """
        * Can change directory group owner.
        * Exit code equals 2 if group owner was changed.
        * Exit code equals 0 if group owner was not changed.

        * Can get current directory group owner.
        * Exit code equals 2.
        """
        self.resource.set_group(self.group)
        self.assertEqual(2, self.resource.code)

        self.resource.set_group(self.group)
        self.assertEqual(0, self.resource.code)

        cur_group = self.resource.get_group()
        self.assertEqual(2, self.resource.code)
        self.assertEqual(self.group, cur_group)


if __name__ == "__main__":
    unittest.main()
