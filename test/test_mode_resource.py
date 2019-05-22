# -*- coding: utf-8 -*-
import unittest

from py_attribute_resource.py_mode_resource import ModeResource
from py_directory_resource import DirectoryResource
from py_file_resource import FileResource


class TestOwnerMode(unittest.TestCase):
    """
    Tests for ModeResource class.
    This test class check that ModeResource class can change owner permission.
    """

    def setUp(self):
        self.resource = ModeResource("test.txt")
        self.fr = FileResource("test.txt")
        self.fr.create()

    def tearDown(self):
        self.fr.delete()

    def test1(self):
        """
        * Can change file permission.
        * Exit code equals 2 if file permission was changed.
        * Exit code equals 0 if file permission was not changed.

        * Can get current file permission.
        * Exit code equals 2.
        """
        self.resource.set_mode(0000)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0000)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual(2, self.resource.code)
        self.assertEqual('0000', cur_mode)

    def test2(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0100)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0100)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0100', cur_mode)

    def test3(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0200)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0200)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0200', cur_mode)

    def test4(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0300)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0300)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0300', cur_mode)

    def test5(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0400)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0400)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0400', cur_mode)

    def test6(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0500)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0500)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0500', cur_mode)

    def test7(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0600)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0600)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0600', cur_mode)

    def test8(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0700)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0700)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0700', cur_mode)


class TestGroupMode(unittest.TestCase):
    """
    Tests for ModeResource class.
    This test class check that ModeResource class can change group permission.
    """

    def setUp(self):
        self.resource = ModeResource("test.txt")
        self.fr = FileResource("test.txt")
        self.fr.create()

    def tearDown(self):
        self.fr.delete()

    def test2(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0010)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0010)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0010', cur_mode)

    def test3(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0020)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0020)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0020', cur_mode)

    def test4(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0030)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0030)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0030', cur_mode)

    def test5(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0040)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0040)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0040', cur_mode)

    def test6(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0050)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0050)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0050', cur_mode)

    def test7(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0060)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0060)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0060', cur_mode)

    def test8(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0070)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0070)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0070', cur_mode)


class TestOthersMode(unittest.TestCase):
    """
    Tests for ModeResource class.
    This test class check that ModeResource class can change others permission.
    """

    def setUp(self):
        self.resource = ModeResource("test.txt")
        self.fr = FileResource("test.txt")
        self.fr.create()

    def tearDown(self):
        self.fr.delete()

    def test2(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0001)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0001)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0001', cur_mode)

    def test3(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0002)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0002)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0002', cur_mode)

    def test4(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0003)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0003)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0003', cur_mode)

    def test5(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0004)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0004)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0004', cur_mode)

    def test6(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0005)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0005)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0005', cur_mode)

    def test7(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0006)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0006)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0006', cur_mode)

    def test8(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_mode(0007)
        self.assertEqual(2, self.resource.code)

        self.resource.set_mode(0007)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_mode()
        self.assertEqual('0007', cur_mode)


class TestAllMode(unittest.TestCase):
    """
    Tests for ModeResource class.
    This test class check that ModeResource class can change
    owner permission, group permission and others permission at the same time.
    """

    def setUp(self):
        self.fr = FileResource("test.txt")
        self.fr.create()

        self.dr = DirectoryResource("test_dir")
        self.dr.create()

    def tearDown(self):
        self.fr.delete()
        self.dr.delete()

    def test1(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        resource = ModeResource("test.txt")
        resource.set_mode(0712)
        self.assertEqual(2, resource.code)

        resource.set_mode(0712)
        self.assertEqual(0, resource.code)

        cur_mode = resource.get_mode()
        self.assertEqual('0712', cur_mode)

    def test2(self):
        """
        * Can change directory permission.
        * Exit code equals 2.
        """
        resource = ModeResource("test_dir")
        resource.set_mode(0617)
        self.assertEqual(2, resource.code)

        resource.set_mode(0617)
        self.assertEqual(0, resource.code)

        cur_mode = resource.get_mode()
        self.assertEqual('0617', cur_mode)


if __name__ == "__main__":
    unittest.main()
