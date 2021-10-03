from iclassification import ParserClassificationInterface
from iparser import FormalParserInterface


@FormalParserInterface.register
@ParserClassificationInterface.register
class EmlParserNew(FormalParserInterface, ParserClassificationInterface):
    """Extract text from an email."""

    category = "EML"
    id = "EmlParserNew"

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        print(self.__class__, "load_data_source", path, file_name)
        return ""

    def extract_text(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        return {}
