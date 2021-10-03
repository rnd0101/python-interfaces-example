"""
This is an interface

from https://realpython.com/python-interface/#formal-interfaces
"""
from abc import abstractmethod
from typing import Type

from interface_meta import InterfaceMeta


class ParserClassificationInterface(metaclass=InterfaceMeta):
    _id_attribute = "id"

    @property
    @abstractmethod
    def category(self):
        """For classification"""

    def get_name(self):
        """Example of concrete method. OK to provide concrete methods when then depend only on other methods
        in the same interface"""
        return self.__class__.__name__


ParserClassificationInterfaceType = Type[ParserClassificationInterface]
