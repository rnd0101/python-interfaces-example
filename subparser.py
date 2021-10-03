from iclassification import ParserClassificationInterface
from iparser import SuccessfulSubFormalParserInterface


@ParserClassificationInterface.register
@SuccessfulSubFormalParserInterface.register
class PdfParserHtml(SuccessfulSubFormalParserInterface, ParserClassificationInterface):
    """Extract html from a PDF."""

    _category = None
    id = "PdfParserHtml"

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        print(self.__class__, "load_data_source", path, file_name)
        return "does not matter"

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        print(self.__class__, "extract_text", full_file_path)
        return {"k": "does not matter"}

    def extract_html(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        print(self.__class__, "extract_text", full_file_path)
        return {"h": "does not matter"}