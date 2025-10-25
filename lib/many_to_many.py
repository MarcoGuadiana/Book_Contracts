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

