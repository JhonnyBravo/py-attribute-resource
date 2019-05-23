# -*- coding: utf-8 -*-
"""
ファイルまたはディレクトリの所有者を管理する。
"""
import os

from pip._vendor.distlib._backport.tarfile import pwd

from py_attribute_resource import AttributeResource
from py_status_resource import StatusResource


class OwnerResource(StatusResource, AttributeResource):
    """
    ファイルまたはディレクトリの所有者を管理する。
    """

    def __init__(self, path):
        """
        :param str path: 操作対象とするファイルまたはディレクトリのパスを指定する。
        """
        StatusResource.__init__(self)
        self.__path = path

    @property
    def path(self):
        """
        :return: 操作対象とするファイルまたはディレクトリのパスを返す。
        :rtype: str
        """
        return self.__path

    def get_attribute(self):
        """
        :return: ファイルまたはディレクトリから現在の所有者を取得する。
        :rtype: str
        """
        owner_name = ""

        if self.is_windows():
            self.print_message(1, "Windows では所有者の取得はサポートしていません。")
            return owner_name

        if not os.path.exists(self.path):
            self.print_message(1, self.path + " が見つかりません。")
            return owner_name

        self.print_message(0, self.path + " の所有者を取得しています。")
        owner_name = pwd.getpwuid(os.stat(self.path).st_uid).pw_name

        self.code = 2
        return owner_name

    def set_attribute(self, owner_name):
        """
        ファイルまたはディレクトリへ新しい所有者を設定する。

        :param str owner_name: 新しい所有者として設定するユーザ名を指定する。
        """
        if self.is_windows():
            self.print_message(1, "Windows では所有者の変更はサポートしていません。")
            return

        if not os.path.exists(self.path):
            self.print_message(1, self.path + " が見つかりません。")

        cur_owner = os.stat(self.path).st_uid
        new_owner = pwd.getpwnam(owner_name).pw_uid

        if cur_owner == new_owner:
            self.code = 0
            return
        else:
            self.print_message(0, self.path + " の所有者を変更しています。")
            os.chown(self.path, new_owner, -1)
            self.code = 2
