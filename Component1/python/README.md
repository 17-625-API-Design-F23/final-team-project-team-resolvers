# Assignment 1 - Python

Welcome to Assignment 1! This is the Python setup repository for Assignment 1. You can find the assignment PDF on Canvas.

## Installation & Setup

To get started, you will need to have Python 3 installed on your machine. If you don't have them installed, you can download them from the official website: https://www.python.org/downloads/

After this, you can create a virtual environment using venv 

```powershell
<venv>\Scripts\Activate.ps1 # for Windows PowerShell
```
or
```bash
source <venv>/bin/activate # for unix based systems 
```
Refer to https://docs.python.org/3/library/venv.html for more information.

Use pip to install pytest and pytest-cov.

```bash
pip install pytest pytest-cov
```

## Assignment

Currently, this is just starter code with a basic test case.
Your task is to implement a REST API for a fitness center, according to the design specifications in the assignment PDF. You are free to use any framework of your choice. We recommend using [Flask](https://flask.palletsprojects.com/en/2.0.x/) as a good starting point.

Once you have created your API, you should also write tests for it. Your tests should hit all the endpoints in your API and should ensure that they are working correctly. Make sure to test both correct and incorrect API calls.


To test - 
```bash
pytest --cov=. --cov-fail-under=100
```

## Submission

To submit your assignment, you should take a (FULL) screenshot of all your tests passing and your code passing linting.

You should then upload your screenshot to the assignment submission page on Gradescope.

Good luck and have fun!
