import os  #The OS module provides functions for interacting with the operating system
import secrets  #The secrets module is used for generating random passwords
import string   #The string module is used for the functions that it contains to process standard Python strings

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" *-- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(f"{bookname} BOOK IS NOT AVAILABLE OR IS TAKEN BY SOMEONE ELSE.\n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED : THANK YOU, KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)

    def addbook(self,bookname):
        self.books.append(bookname)
        

    def removebook(self,bookname):
        self.books.remove(bookname)
            

class help_info():
    def clearConsole(self):
        print('\n' * 20)
        print("The password will be randomly generated")
        print('\n' * 3)
    def helpInformation(self):
        print("=====================")
        print("Help Information")
        print("For any thechnical support please contact 002133375184")
        print("Alternatively send and email to Help.Info@mylibrary.com ")
        print("=====================")

class admin(Library):
    def __init__(self,listOfBooks):
        super().__init__(listOfBooks)
    def addbook(self):
        new_Name = input("Enter the Name of new book : ").title()
        # title method converts first letter of every word in the string in upper case
        return new_Name     
    def removebook(self):   
        self.name = input("\nEnter the Name of the book : ").title()
        return self.name
       
class Book():
    def userDisplay(self):
        print("\t\t\t******* WELCOME TO THE LIBRARY *******\n")
        print("""CHOOSE WHAT DO YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Track books\n5. exit the library\n""")
    def adminDisplay(self):
        print("\t\t\t******* WELCOME TO THE LIBRARY *******\n")
        print("""CHOOSE WHAT DO YOU WANT TO DO:-\n1. Listing all books\n2. Add Book\n3. Remove Book\n4. exit\n""")
        
class User():
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ").title()
        # title method converts first letter of every word in the string in upper case
        return self.book    

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ").title()
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book


if __name__ == "__main__":
    
    Password = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(4)))
    
    listOfBooks = ["Code: The Hidden Language of Computer Hardware and Software",
                   "Code Complete: A Practical Handbook of Software Construction",
                   "Computer Science","Clean Code: A Handbook of Agile Software Craftsmanship",
                   "Thinking in Systems: A Primer", "Foundations of Computer Science",
                   "The Soul of a New Machine", "Superintelligence: Paths, Dangers, Strategies",
                   "Types and Programming Languages","Algorithms"]
    
    Mylibrary = Library(listOfBooks)
    user = User()
    adm = admin(listOfBooks)
    d = Book()
    track = []
    c = help_info()
    c.helpInformation()
    input("Press Enter To Continue..... ")
    c.clearConsole()
    tp = input("Login Admin/Login User [Type A to Login in the Admin/ Type U to Login in the User] : ")
    if tp == 'A' or tp == 'a':
        print("The password is: " + Password)
        password = input("Enter the password : ")
        if password == Password:
            d.adminDisplay()
            while (True):
                
                try:
                    usr_response = int(input("Enter your choice: "))

                    if usr_response == 1:  # listing all available books
                        Mylibrary.displayAvailableBooks()
                    elif usr_response == 2:  # add a book
                        Mylibrary.addbook(adm.addbook())
                        Mylibrary.displayAvailableBooks()
                        print("BOOK ADDED\n")
                        
                    elif usr_response == 3:  # delete a book
                        Mylibrary.removebook(adm.removebook())
                        Mylibrary.displayAvailableBooks()
                        print("BOOK REMOVED\n")
                    elif usr_response == 4: #exit
                        print("THANK YOU ! \n")
                        exit()
                    else:
                        print("INVALID INPUT! \n")
                except Exception as e:              
                    print(f"{e}---> INVALID INPUT!! \n")


    elif tp == 'U' or tp == 'u':
        print("The password is: " + Password)
        password = input("Enter the password : ")
        if (password == Password):
            d.userDisplay()
            while (True):
                try:
                    usr_response = int(input("Enter your choice: "))

                    if usr_response == 1:  # listing all available books
                        Mylibrary.displayAvailableBooks()
                    elif usr_response == 2:  # borrow a book
                        Mylibrary.borrowBook(input("Enter your name: "), user.requestBook())
                    elif usr_response == 3:  # return a book
                        Mylibrary.returnBook(user.returnBook())
                    elif usr_response == 4:  # track books
                        for i in track:
                            for key, value in i.items():
                                holder = key
                                book = value
                                print(f"{book} book is taken by {holder}.")
                        print("\n")
                        if len(track) == 0:
                            print("NO BOOKS ARE ISSUED!. \n")
                    
                    elif usr_response == 5: #exit
                        print("THANK YOU ! \n")
                        exit()
                    else:
                        print("INVAILD INPUT! \n")
                except Exception as e:              
                    print(f"{e}---> INVAILD INPUT!! \n")


        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")        