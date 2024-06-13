class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


# Example test code
if __name__ == "__main__":
    author = Author("John")
    book = Book("Python Programming")
    contract = author.sign_contract(book, "01/01/2021", 50)

    assert author.name == "John"
    assert book.title == "Python Programming"
    assert contract.author == author
    assert contract.book == book
    assert contract.date == "01/01/2021"
    assert contract.royalties == 50
    assert author.contracts() == [contract]
    assert author.books() == [book]
    assert book.contracts() == [contract]
    assert book.authors() == [author]
    assert author.total_royalties() == 50
    assert Contract.contracts_by_date("01/01/2021") == [contract]
