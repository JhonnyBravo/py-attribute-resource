# -*- coding: utf-8 -*-
"""
ファイルまたはディレクトリのパーミッション設定を管理する。
"""
import os

from pip._vendor.distlib._backport.tarfile import pwd

from py_attribute_resource import AttributeResource
from py_status_resource import StatusResource


class ModeResource(StatusResource, AttributeResource):
    """
    ファイルまたはディレクトリのパーミッション設定を管理する。
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
        :return: ファイルまたはディレクトリから現在のパーミッション設定を取得する。
        :rtype: str
        """
        mode = 0000

        if self.is_windows():
            self.print_message(1, "Windows ではパーミッションの取得はサポートしていません。")
            return mode

        if not os.path.exists(self.path):
            self.print_message(1, self.path + " が見つかりません。")
            return mode

        self.print_message(0, self.path + " のパーミッションを取得しています。")
        mode = oct(os.stat(self.path).st_mode)[-4:]

        self.code = 2
        return mode

    def set_attribute(self, mode):
        """
        ファイルまたはディレクトリのパーミッション設定を変更する。

        :param int mode: 新しいパーミッション値として設定する値を 4 桁の 8 進数で指定する。
        """
        if self.is_windows():
            self.print_message(1, "Windows ではパーミッションの変更はサポートしていません。")
            return

        if not os.path.exists(self.path):
            self.print_message(1, self.path + " が見つかりません。")

        cur_mode = int(oct(os.stat(self.path).st_mode)[-4:], 8)

        if cur_mode == mode:
            self.code = 0
            return
        else:
            self.print_message(0, self.path + " のパーミッションを変更しています。")
            os.chmod(self.path, mode)
            self.code = 2
