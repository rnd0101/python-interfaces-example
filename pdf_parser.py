from iclassification import ParserClassificationInterface
from iparser import FormalParserInterface


@ParserClassificationInterface.register
@FormalParserInterface.register
class PdfParserNew(FormalParserInterface, ParserClassificationInterface):
    """Extract text from a PDF."""

    category = "PDF"
    id = "PdfParserNew"

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        print(self.__class__, "load_data_source", path, file_name)
        return "does not matter"

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        print(self.__class__, "extract_text", full_file_path)
        return {"k": "does not matter"}


@ParserClassificationInterface.register
@FormalParserInterface.register
class PdfParserNewest(PdfParserNew):
    """Extract text from a PDF."""
    id = "PdfParserNewest"

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        print(self.__class__, "load_data_source", path, file_name)
        return "does not matter"
