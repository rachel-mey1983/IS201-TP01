# IS201 Fundamentals of Computing – Python

HOS02 – Python Data Type, Conversion, and Data Structure
03/21/2024 Developed by Scott Zhou
04/01/2024 reviewed by Vaishnavi Mandage
School of Technology and Computing (STC) @City University of Seattle (CityU)

Before You Start
• Version numbers may not match the most current version at the time of writing. If given the option to choose between the stable release (long-term support) or the most recent, please select the stable release rather than the beta-testing version.
• Screenshots may be different from your environment.
• There might be subtle discrepancies along the steps. Please use your best judgment while going through this cookbook-style tutorial to complete each step.  For your working directory, use your course number. This tutorial may use a different course number as an example.
• The directory path shown in screenshots may be different from yours.  
• If you are not sure what to do or confused with any steps:  

1. Consult the resources listed below.
2. If you cannot solve the problem after a few tries, ask a TA for help.  

Learning Outcomes
Students will be able to:
• Understand the Python data types and casting
• Understand the Arrays and Enums

Create a Project

Follow HOS1 to set up the project in Codespaces, or use any other code editor you prefer, such as Visual Studio, Visual Studio Code, Sublime, Vim, etc…

We will create a Python project to cover all the learning outcomes; the project simulates a library management system, which will store book categories as enum and store books in a list.

1. Create a Python file named HOS02.py
2. Import Enum from Enum; this will load the required module for this program; in this case, it is an enumeration.

3. Define book categories using enumeration; there are four categories: fiction, nonfiction, educational, and children.

4. Define a book class consisting of title, author, and category.

5. Create a library class and initialize a list to store all the books.

6. Create two books to test if the list and enums work properly for books and book categories.

7. Create a third book to practice casting category numbers to category enum.

8. Initialize the library object and add all three books.

9. Call the display_books()method from the library to verify all the books have been added.

10. The expected output in the terminal after executing the program:

Submit your Work to Brightspace

Please upload your .py file to the HOS02 assignment on Brightspace.
