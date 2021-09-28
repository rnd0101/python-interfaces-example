from iparser import SuccessfulSubFormalParserInterface


class HTML5Parser(SuccessfulSubFormalParserInterface):
    def extract_html(self, full_file_path: str) -> dict:
        pass

    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_path: str) -> dict:
        pass