# Test-Driven Development with Python
Code written based on the 'TDD with Python' book by Harry J.W. Percival, a great introduction to TDD, Django and Selenium. 

To follow the book, visit https://www.obeythetestinggoat.com

### About:
This project provides the code to run a webapp that allows a user to make a to-do list. The user can add items to their to-do list, mark them completed and a custom URL is generated that allows an user to get back to their to-do list. 

The project is written in Python 3.6 and uses Django as its web framework and Selenium to automate some browser controls for testing purposes. 

### Installation:
If you'd like to run this project locally, you'll need to have Python 3.6(+) and Git installed. 

You can pull this repository, create a virtual environment and install the requirements using the following commands in your command prompt / terminal in your project folder*:

```
C:\Python scripts> git clone git@github.com:MarkHurenkamp/TDDBook.git
C:\Python scripts> cd TDDBook
C:\Python scripts\TDDBook> python -m venv venv
C:\Python scripts\TDDBook> venv\scripts\activate
(venv) C:\Python scripts\TDDBook> pip install -r requirements.txt
```

Then start the server:
```
(venv) C:\Python scripts\TDDBook> python manage.py runserver
```

Then open your browser and navigate to http://localhost:8000

Press CTRL-C in the command prompt / terminal to stop the server.

**commands may vary slightly depending on your operating system*