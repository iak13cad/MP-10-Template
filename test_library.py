import pytest
import random
import assessMeTester_StringSimilarity
#TO RUN pytest --tb=short -s

import library

def test_book_class(capsys, monkeypatch, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_book_class"
        className = "class Book"
          
        try:

            # invoke
            book1 = library.Book("The Catcher in the Rye", "J.D. Salinger", 3)
            
            ##check the default attributes
            attributesOk = True

            #Before any attribute test, put assert message if 
            assertMessage="Attribute error: title\n"
            if book1.title != "The Catcher in the Rye":
                attributesOk=False
            assertMessage="Attribute error: author\n"
            if book1.author != "J.D. Salinger":
                attributesOk=False
            assertMessage="Attribute error: copies\n"
            if book1.copies != 3:
                attributesOk=False
          
            assertMessage=""
            # Part for string comparison!
            if attributesOk==True:
                
                assert True
            else:
                success = False
                assertMessage=f"The {className} is not correct!\n"
                assertMessage = f"The defaut value or attribute types are not properly defined!"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage


def test_book_str(capsys, monkeypatch, printFeedback=True):

        
    expected_output1 = """Title: The Catcher in the Rye, Author: J.D. Salinger, Copies available: 3"""
    
    # Execute the function
      # Run the main function
    book1 = library.Book("The Catcher in the Rye", "J.D. Salinger", 3)
    print(book1)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score1 = assessMeTester_StringSimilarity.string_similarity(expected_output1, captured.out)
  
   
    if similarity_score1 >= similarity_threshold: 
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score1 * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************test_book_str tester failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output1+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score1})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")
  

    assert similarity_score1 >= similarity_threshold, f"Strings are not similar enough (score: {similarity_score1})"



def test_member_class(capsys, monkeypatch, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_member_class"
        className = "class Member"
          
        try:

            # invoke
            book1 = library.Book("The Catcher in the Rye", "J.D. Salinger", 3)
           
            member1 = library.Member("Alice",[book1])
            print(member1)
            
            ##check the default attributes
            attributesOk = True

            #Before any attribute test, put assert message if 
            assertMessage="Attribute error: name\n"
            if member1.name != "Alice":
                attributesOk=False
            assertMessage="Attribute error: borrowed_books\n"
            if type(member1.borrowed_books) != list:
                attributesOk=False
                   
            assertMessage=""
            # Part for string comparison!
            if attributesOk==True:
                
                assert True
            else:
                success = False
                assertMessage=f"The {className} is not correct!\n"
                assertMessage = f"The defaut value or attribute types are not properly defined!"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage




def test_member_str(capsys, monkeypatch, printFeedback=True):

        
    expected_output1 = """Member: Alice, Borrowed Books: ['The Catcher in the Rye', 'To Kill a Mockingbird', '1984']"""
    
    # Execute the function
      # Run the main function
    book1 = library.Book("The Catcher in the Rye", "J.D. Salinger", 3)
    book2 = library.Book("To Kill a Mockingbird", "Harper Lee", 5)
    book3 = library.Book("1984", "George Orwell", 2)

    books = [book1,book2,book3]

    member1 = library.Member("Alice",books)
    print(member1)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.90  # Set your desired threshold here

    similarity_score1 = assessMeTester_StringSimilarity.string_similarity(expected_output1, captured.out)
  
   
    if similarity_score1 >= similarity_threshold: 
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score1 * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************test_member_str tester failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output1+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score1})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")
  

    assert similarity_score1 >= similarity_threshold, f"Strings are not similar enough (score: {similarity_score1})"
