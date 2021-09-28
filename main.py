"""
Exploring meta-classes / interfaces using example from

https://stackoverflow.com/questions/62863661/how-to-overload-same-named-methods-of-different-interfaces-with-type-annotations

"""
from __future__ import annotations

from email_parser import EmlParserNew
from iclassification import ParserClassificationInterface
from iparser import FormalParserInterface
from iparser import SubFormalParserInterface
from iparser import SuccessfulSubFormalParserInterface
from pdf_parser import PdfParserNew
from pdf_parser import PdfParserNewest
from subparser import PdfParserHtml


def get_classification() -> (ParserClassificationInterface | FormalParserInterface):
    return ParserClassificationInterface.for_id("PdfParserNew")()


if __name__ == "__main__":
    print(issubclass(PdfParserNew, FormalParserInterface))
    parser = PdfParserNew()
    pdf_parser = parser
    pdf_parser.load_data_source("", "")
    parser1 = PdfParserNewest()
    pdf_parser2 = parser1
    pdf_parser2.load_data_source("", "")
    parser2 = EmlParserNew()
    eml_parser = parser2
    eml_parser.load_data_source("", "")

    print(FormalParserInterface.all_classes())
    print(ParserClassificationInterface.all_classes())

    some_parser = get_classification()
    print(some_parser.load_data_source("", ""))
    print(FormalParserInterface.for_id("PdfParserNew")().load_data_source("", ""))

    print(pdf_parser.category)
    print(pdf_parser2.category)
    print(eml_parser.category)
    print(eml_parser.get_name())
    print(pdf_parser.get_name())

    print("isinstance", isinstance(pdf_parser2, ParserClassificationInterface))
    print("isinstance", isinstance(pdf_parser2, FormalParserInterface))
    print("issubclass", issubclass(PdfParserNew, ParserClassificationInterface))
    print("issubclass", issubclass(PdfParserNewest, FormalParserInterface))

    print(ParserClassificationInterface._dump_registry())

    try:
        sub_parser = SubFormalParserInterface()
    except TypeError as e:
        print(f"Error expected: {e}")

    pdf_html_parser = PdfParserHtml()
    pdf_html_parser.load_data_source("", "")
    print("isinstance", isinstance(pdf_html_parser, ParserClassificationInterface))
    print("isinstance", isinstance(pdf_html_parser, FormalParserInterface))
    print("isinstance", isinstance(pdf_html_parser, SuccessfulSubFormalParserInterface))

    # Interface inheritance also logical from registration point of view:

    print(FormalParserInterface.for_id("PdfParserHtml")())
    print(SuccessfulSubFormalParserInterface.for_id("PdfParserHtml")())
    print(SuccessfulSubFormalParserInterface.for_id("PdfParserNew") is None)
    print(FormalParserInterface.all_classes())
    print(SuccessfulSubFormalParserInterface.all_classes())
    print(ParserClassificationInterface.all_classes())
