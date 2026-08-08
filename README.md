In this project, I focused on building the application using a simple and clear approach to make sure I fully understand each part of the system rather than relying
on complex patterns or external libraries.

Models (models.py)
I used a Contact class to represent each contact. It includes basic attributes such as name, phone, email, group andd added. I also used helper methods like
to_dict() and from_dict() to easily convert between objects and JSON format for storage.

Repository Layer (repository.py)
this included all operations such as add, find, update, delete and are handled using a list of Contact objects. I used simple loops for searching instead of advanced 
data structures to keep the logic easy to understand and follow.

Storage (storage.py)
For data persistence, I used a JSON file stored in a data/ directory. I handled reading and writing using Python’s built-in json module, specifically:
->json.load() to read data from the file  
->json.dump() to save data back to the file  
This helped me better understand how data is stored and retrieved in a real application.

CLI (cli.py)
The user interface is a command-line menu. I implemented a simple numbered menu system that allows the user to navigate between options easily. All input and output 
are handled in this layer to maintain separation of concerns.

Validation (validation.py)
I implemented input validation manually to ensure correct data entry.This includes:
->checking for non-empty names  
-> validating email format  
->validating phone numbers  
Here for email and phone validation, I used regular expressions to ensure the format is correct.

#Sorting & Searching
Contacts are sorted using Python’s built-in sorted() function based on last name then first name. Searching is implemented using case-insensitive partial matching 
across name, phone, and email fields.

Type Hints
I used type hints in my functions to make the code clearer and easier to understand.

Error Handling
I used basic try/except blocks, especially in file handling, to prevent the program from crashing and to handle cases like missing or corrupted files.

Testing (tests/)
I used pytest to test the main functionality of the application, including models, repository, storage, and validation. The tests focus on core functionality to ensure
the system works as expected.

Code Quality
I used Ruff to check code style and ensure it follows clean coding practices such as consistent formatting and proper structure.
