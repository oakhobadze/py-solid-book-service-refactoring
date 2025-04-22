from typing import Type
from books import Book
from serializer import SerializerJson, SerializerXml, Serializer
from display import DisplayConsole, DisplayReverse, Display
from printer import PrinterConsole, PrinterReverse, Printer

DISPLAYS: dict[str, Type[Display]] = {
    "console": DisplayConsole,
    "reverse": DisplayReverse,
}

PRINTERS: dict[str, Type[Printer]] = {
    "console": PrinterConsole,
    "reverse": PrinterReverse,
}

SERIALIZERS: dict[str, Type[Serializer]] = {
    "json": SerializerJson,
    "xml": SerializerXml,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAYS[method_type]().display(book.content)
        elif cmd == "print":
            PRINTERS[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZERS[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
