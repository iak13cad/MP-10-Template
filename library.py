
'''
Object-Oriented Library!

@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: MiniPracticum 10
@ASSESSME.ANALYZE: YES
'''

'''
Create a Python class named "Book."

 - The class should have an __init__ method that takes three parameters: title:str, author:str, and copies:int. 

 - Inside the __init__ method, initialize instance variables to store the title, author, and copies. 
 Make sure that you use the provided parameter names.

- Define a __str__ method within the class. 
This method should return a string representation of the book in the following format:

Title: [title], Author: [author], Copies available: [copies]

replace [title], [author], and [copies] with the actual values of the respective instance variables.


Example: See in the main()

'''
class Book:
    pass


'''
Create a Python class named "Member."

The class should have an __init__ method that takes two parameters: name (a string) and borrowed_books (a list of Book objects). 
Inside the __init__ method, initialize instance variables to store the name and the list of borrowed books. 
Make sure to use the provided parameter names.

Define a __str__ method within the class. 
This method should return a string representation of the member in the following format:

Member: [name], Borrowed Books: [list_of_borrowed_book_titles]

Replace [name] with the actual member's name, and [list_of_borrowed_book_titles] with a comma-separated list of titles of the borrowed books.

'''
class Member:
    pass


# Example usage
if __name__ == "__main__":

    book1 = Book("The Catcher in the Rye", "J.D. Salinger", 3)
    print(book1) #returns "Title: The Catcher in the Rye, Author: J.D. Salinger, Copies available: 3" 


    book2 = Book("To Kill a Mockingbird", "Harper Lee", 5)
    book3 = Book("1984", "George Orwell", 2)
    books = [book1,book2,book3]

    member1 = Member("Alice",books)
    print(member1)# returns Member: Alice, Borrowed Books: ['The Catcher in the Rye', 'To Kill a Mockingbird', '1984']



    
