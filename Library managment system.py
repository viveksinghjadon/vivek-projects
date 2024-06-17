class Book:
    def __init__(self,*title,status):
        self.title=title
        self.status=status
        
class Library:
    def __init__(self):
        self.booklist=[]
    def add_book(self,title):
        new_book=Book(title)
        self.booklist.append(new_book)
        print(f"book '{title}'added to the library")
    def remove_book(self,title):
        for book in self.booklist:
            if book.title==title:
                self.booklist.remove(book)
                print(f"book '{title}'removed from the library")
            else:
                print(f"book '{title}'not found in the library")
    def search_book(self,title):
        for book in self.booklist:
            if book.title==title:
                print(f"book '{title}'found in the library")
            else:
                print(f"book '{title}'not found in the library")
    def borrow_book(self,title):
        for book in self.booklist:
            if book.title==title:
                if book.status==True:
                    book.status="borrowed"
                    print(f"book '{title}'borrowed from the library")
                else:
                    print(f"book '{title}'not found in the library")
    def return_book(self,title):
        for book in self.booklist:
            if book.title==title:
                if book.status=="borrowed":
                    book.status=True
                    print(f"book '{title}'returned to the library")
                else:
                    print(f"book '{title}'not found in the library")

a=Library()
while True:
        print("Library")
        print("1.Add book")
        print("2.Remove book")
        print("3.Search book")
        print("4.Borrow book")
        print("5.Return book")
        print("6.Exit")
        choice =int(input("Enter your choice:"))
        if choice== 1:
            title=input("Enter the title of the book:")
            a.add_book(title)
        elif choice== 2:
            title=input("Enter the title of the book:")
            a.remove_book(title)
        elif choice== 3:
            title=input("Enter the title of the book:")
            a.search_book(title)
        elif choice== 4:
            title=input("Enter the title of the book:")
            a.borrow_book(title)
        elif choice== 5:
            title=input("Enter the title of the book:")
            a.return_book(title)
        elif choice== 6:
            break
        else:
            print("Invalid choice")
    
