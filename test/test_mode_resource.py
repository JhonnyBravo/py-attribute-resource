# -*- coding: utf-8 -*-
import platform
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

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test1(self):
        """
        * Can change file permission.
        * Exit code equals 2 if file permission was changed.
        * Exit code equals 0 if file permission was not changed.

        * Can get current file permission.
        * Exit code equals 2.
        """
        self.resource.set_attribute(0000)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0000)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual(2, self.resource.code)
        self.assertEqual('0000', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test2(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0100)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0100)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0100', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test3(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0200)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0200)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0200', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test4(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0300)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0300)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0300', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test5(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0400)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0400)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0400', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test6(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0500)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0500)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0500', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test7(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0600)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0600)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0600', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test8(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0700)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0700)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
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

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test2(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0010)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0010)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0010', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test3(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0020)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0020)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0020', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test4(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0030)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0030)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0030', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test5(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0040)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0040)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0040', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test6(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0050)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0050)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0050', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test7(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0060)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0060)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0060', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test8(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0070)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0070)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
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

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test2(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0001)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0001)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0001', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test3(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0002)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0002)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0002', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test4(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0003)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0003)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0003', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test5(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0004)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0004)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0004', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test6(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0005)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0005)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0005', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test7(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0006)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0006)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
        self.assertEqual('0006', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test8(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        self.resource.set_attribute(0007)
        self.assertEqual(2, self.resource.code)

        self.resource.set_attribute(0007)
        self.assertEqual(0, self.resource.code)

        cur_mode = self.resource.get_attribute()
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

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test1(self):
        """
        * Can change file permission.
        * Exit code equals 2
        """
        resource = ModeResource("test.txt")
        resource.set_attribute(0712)
        self.assertEqual(2, resource.code)

        resource.set_attribute(0712)
        self.assertEqual(0, resource.code)

        cur_mode = resource.get_attribute()
        self.assertEqual('0712', cur_mode)

    @unittest.skipIf(platform.system() == "Windows", "Not supported on Windows.")
    def test2(self):
        """
        * Can change directory permission.
        * Exit code equals 2.
        """
        resource = ModeResource("test_dir")
        resource.set_attribute(0617)
        self.assertEqual(2, resource.code)

        resource.set_attribute(0617)
        self.assertEqual(0, resource.code)

        cur_mode = resource.get_attribute()
        self.assertEqual('0617', cur_mode)


class TestWindows(unittest.TestCase):
    """
    Tests for Windows.
    """

    def setUp(self):
        self.resource = ModeResource("test.txt")
        self.fr = FileResource("test.txt")
        self.fr.create()

    def tearDown(self):
        self.fr.delete()

    @unittest.skipIf(platform.system() != "Windows", "Test for Windows.")
    def test1(self):
        """
        Exit code equals 1 if platform equals Windows.
        """
        mode = self.resource.get_attribute()
        self.assertEqual(1, self.resource.code)
        self.assertFalse(mode)

    @unittest.skipIf(platform.system() != "Windows", "Test for Windows.")
    def test2(self):
        """
        Exit code equals 1 if platform equals Windows.
        """
        self.resource.set_attribute(0761)
        self.assertEqual(1, self.resource.code)


if __name__ == "__main__":
    unittest.main()
