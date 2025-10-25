class Book:
    
    all = []

    def __init__(self, title: str):
       
        self.title = title
        Book.all.append(self)

    def contracts(self):
        
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
       
        return list(set([contract.author for contract in self.contracts()]))

class Author:
   
    all = []

    def __init__(self, name: str):
        
        self.name = name
        Author.all.append(self)

    def contracts(self):
        
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book: Book, date: str, royalties: int):
       
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    
    all = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of the Author class.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of the Book class.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer.")
        self._royalties = value

    

    @classmethod
    def contracts_by_date(cls, date: str):
        
        return [contract for contract in cls.all if contract.date == date]
