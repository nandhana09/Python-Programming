class Publisher:
    def __init__(self,publisher_name):
        self.publisher_name=publisher_name
    def display(self):
        pass
class Book(Publisher):
    def __init__(self,publisher_name,title,author):
         Publisher.__init__(self,publisher_name)
         self.title=title
         self.author=author
    def display(self):
        pass
class Python(Book):
    def __init__(self,publisher_name,title,author,price,no_of_pages):
        Book.__init__(self,publisher_name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Publisher Name=",self.publisher_name)
        print("title=",self.title)
        print("Author=",self.author)
        print("Book Price=",self.price)
        print("No:of Pages=",self.no_of_pages)
p=Python("PEARSON EDUCATION","CORE PYTHON APPLICATION PROGRAMMING","WESLEY J.CHUN",400,1500)
p.display()
                 
    
        
