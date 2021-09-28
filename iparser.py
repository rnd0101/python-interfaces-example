"""
This is an interface

from https://realpython.com/python-interface/#formal-interfaces
"""

from abc import abstractmethod
from typing import Type

from interface_meta import InterfaceMeta


class FormalParserInterface(metaclass=InterfaceMeta):

    @abstractmethod
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the data set"""

    @abstractmethod
    def extract_text(self, full_file_path: str) -> dict:
        """Extract text from the data set"""


FormalParserInterfaceType = Type[FormalParserInterface]


class SubFormalParserInterface(FormalParserInterface):  # * this is anti-example
    def extract_text(self, full_file_path: str):
        return full_file_path


class SuccessfulSubFormalParserInterface(FormalParserInterface):
    @abstractmethod
    def extract_html(self, full_file_path: str) -> dict:
        """Extract html from the data set"""
        return {}
