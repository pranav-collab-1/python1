class Libraryitem:
    def __init__(self,title,item_id):
        self.title = title
        self.item_id = item_id
    def display(self):
        print(f"Title: {self.title}, Item ID: {self.item_id}")
class Book(Libraryitem):
    def __init__(self,title,item_id,author):
        super().__init__(title,item_id)
        self.author = author
    def display(self):
        super().display()
        print(f"Author: {self.author}")
class Magazine(Libraryitem):
    def __init__(self,title,item_id,issue_number):
        super().__init__(title,item_id)
        self.issue_number = issue_number
    def display(self):
        super().display()
        print(f"Issue Number: {self.issue_number}")
book1 = Book("The Great Gatsby", 101, "F. Scott Fitzgerald")
magazine1 = Magazine("National Geographic", 202, "March 2024")

book1.display()
magazine1.display()
