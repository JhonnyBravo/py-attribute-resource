# -*- coding: utf-8 -*-
"""
ファイルまたはディレクトリの属性を管理する。
"""
from abc import ABCMeta, abstractmethod
import platform


class AttributeResource(object):
    """
    ファイルまたはディレクトリの属性を管理する。
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_attribute(self):
        """
        ファイルまたはディレクトリから属性を取得する。
        """
        pass

    @abstractmethod
    def set_attribute(self, attribute):
        """
        ファイルまたはディレクトリへ属性を設定する。
        """
        pass

    def is_windows(self):
        """
        :return: OS が Windows である場合に True を返し、 Windows ではない場合に False を返す。
        :rtype: bool
        """
        result = False

        if platform.system() == "Windows":
            result = True

        return result
