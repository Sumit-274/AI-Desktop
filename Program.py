import time

class Library:

    def __init__(self,Library_Name,Book_List):
        self.Name = Library_Name
        self.Books_List = []
        self.Books_List.append(Book_List)
        self.Lend_Book_History = {}

    def Display_Book(self):
        for item in self.Books_List:
            print(item)

    def Add_Book(self,Book_Name):
        self.BookName = Book_Name
        self.Books_List.append(self.BookName)
        return f"Thank Mr/Mrs For Donating Book In Our {self.Name} Library"

    def Lend_Book(self,Bookname,Bookowner):
        self.Bookname = Bookname
        self.Owner = Bookowner
        self.Lend_Book_History.update({self.BookName:[self.Owner,time.asctime(time.localtime(time.time))]})
        for item,time in self.Lend_Book_History.items():
            pass
        return "This book {} is Given to this person {} at {}".format(Bookname,time[0],time[1])

Obj = Library()