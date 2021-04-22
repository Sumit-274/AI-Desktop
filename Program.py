import time
class Library:

    def __init__(self,Library_Name,Book_List):
        self.Name = Library_Name
        self.Books_List = []
        self.Books_List.extend(Book_List)
        self.Lend_Book_History = {}

    def Display_Book(self):
        for item in self.Books_List:
            print(item)

    def Add_Book(self,Book_Name):
        self.BookName = Book_Name
        self.Books_List.append(self.BookName)
        return f"Thank Mr/Mrs For Donating Book In Our {self.Name} Library"

    def Lend_Book(self,Bookname,Bookowner):
        self.lenging_Bookname = Bookname
        self.Owner = Bookowner

        if (self.lenging_Bookname in self.Books_List):
            self.Lend_Book_History.update({self.lenging_Bookname:self.Owner})
            return "This book {} is lended".format(self.lenging_Bookname)
            self.Books_List.pop(self.lenging_Bookname)

        else:
            return "Sorry This book is not Available at this time"

        for item,time in self.Lend_Book_History.items():
            pass
        return "This book {} is Given to this person {} at {}".format(Bookname,time[0],time[1])

    def store_Details(self):
        return f"Store name is {self.Name}"

    def return_Book(self,BookName):
        self.return_book = BookName
        if (self.return_book in self.Lend_Book_History.keys()):
            self.Lend_Book_History.pop(self.return_book)
            return "This book {} Have been Returned".format(self.return_book)
        else:
            return "Sorry, But We think this book is not lended by you"
        
Obj = Library("Prakash Library",["Rich dad poor son","Python machine learning","C & c++ ai development"])


def Main():

    print("What you want\n1. Add Book\n2. Lend Book\n3. Return Book\n4. Display Books\n5. Store Details\n6. Exit" )
    ask = int(input("Enter the number\n"))

    if ask == 1:
        book_name = input("Enter the Book Name\n")
        book_name.lower()
        book_name.capitalize()
        Obj.Add_Book(book_name)
    
    elif ask == 2:
        book__name = input("Enter the book name\n")
        book__name.lower()
        book__name.capitalize()
        book__owner = input("Enter your name\n")
        book__owner.lower()
        book__owner.capitalize()
        Obj.Lend_Book(book__name,book__owner)

    elif ask == 3:
        returning_book_name = input("Enter the book name\n")
        returning_book_name.lower()
        returning_book_name.capitalize()
        Obj.return_Book(returning_book_name)

    elif ask == 4:
        Obj.Display_Book()

    elif ask == 5:
        Obj.store_Details()
    
    elif ask == 6:
        exit()

if __name__ == "__main__":
    while True:
        Main()
        time.sleep(5)