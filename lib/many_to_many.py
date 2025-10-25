class Book:
    
    all = []

    def __init__(self, title: str):
       
        self.title = title
        Book.all.append(self)

    def contracts(self):
        
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
       
        return list(set([contract.author for contract in self.contracts()]))

