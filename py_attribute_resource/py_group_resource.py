# -*- coding: utf-8 -*-
"""
ファイルまたはディレクトリのグループ所有者を管理する。
"""
import os

from pip._vendor.distlib._backport.tarfile import grp

from py_status_resource import StatusResource


class GroupResource(StatusResource):
    """
    ファイルまたはディレクトリのグループ所有者を管理する。
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

    def get_group(self):
        """
        :return: ファイルまたはディレクトリから現在のグループ所有者を取得する。
        :rtype: str
        """
        group_name = ""

        if not os.path.exists(self.path):
            self.print_message(1, self.path + " が見つかりません。")
            return group_name

        self.print_message(0, self.path + " のグループ所有者を取得しています。")
        group_name = grp.getgrgid(os.stat(self.path).st_gid).gr_name

        self.code = 2
        return group_name

    def set_group(self, group_name):
        """
        ファイルまたはディレクトリへ新しいグループ所有者を設定する。

        :param str group_name: 新しいグループ所有者として設定するグループ名を指定する。
        """
        if not os.path.exists(self.path):
            self.print_message(1, self.path + " が見つかりません。")

        cur_group = os.stat(self.path).st_gid
        new_group = grp.getgrnam(group_name).gr_gid

        if cur_group == new_group:
            self.code = 0
            return
        else:
            self.print_message(0, self.path + " のグループ所有者を変更しています。")
            os.chown(self.path, -1, new_group)
            self.code = 2
