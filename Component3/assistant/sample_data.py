"""This class provides sample data for the bithub services."""
class SampleData:
    PR_description_list = [
        "This PR adds a new feature that improves user authentication and adds two-factor authentication support.",
        "Fixes a critical bug where the application crashes when processing large datasets.",
        "Refactoring codebase for better maintainability and readability. No functional changes.",
        "Updates the README.md file with clear installation and usage instructions.",
        "Updates external libraries to the latest versions to address security vulnerabilities.",
        "Optimizes database queries for faster response times, improving overall application performance.",
        "Enhances the user interface by redesigning the navigation menu for improved usability.",
        "Adds unit tests for core functionality and increases test coverage to 90%.",
        "Adds support for French and Spanish translations for the application interface.",
        "Addresses a security vulnerability by implementing input validation and escaping user inputs."
    ]
    
    auto_completion_code_list = [
        """
        def calculate_square(x):
            return x * x
        """,

        """
        function greet(name) {
            console.log(`Hello, ${name}!`);
        }
        """,

        """
        public class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }
        }
        """,

        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Sample Page</title>
        </head>
        <body>
            <h1>Welcome to our website</h1>
            <p>This is a sample page.</p>
        </body>
        </html>
        """,

        """
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        """,

        """
        fruits = ["apple", "banana", "cherry", "date"]
        """,

        """
        const colors = ["red", "green", "blue", "yellow"];
        """,

        """
        public int add(int a, int b) {
            return a + b;
        }
        """,

        """
        SELECT * FROM customers WHERE country = 'USA';
        """,

        """
        #include <iostream>

        void say_hello() {
            std::cout << "Hello, world!" << std::endl;
        }
        """
    ]

    gpt_response_list = [
        """
        Needs clarification on your description! Please provide more details.
        """,
        """
        def calculate_average(numbers):
            if not numbers:
                return 0
            return sum(numbers) / len(numbers)
        """,

        """
        import pandas as pd
        data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 22]}
        df = pd.DataFrame(data)
        print(df)
        """,

        """
        const fruits = ['apple', 'banana', 'cherry'];
        for (let fruit of fruits) {
            console.log(fruit);
        }
        """,

        """
        public class Calculator {
            public static int add(int a, int b) {
                return a + b;
            }
        }
        """,

        """
        <form action="/submit" method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <button type="submit">Submit</button>
        </form>
        """,

        """
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n-1)
        """,

        """
        const colors = {
            red: '#FF0000',
            green: '#00FF00',
            blue: '#0000FF'
        };
        console.log(colors['red']);
        """,

        """
        // SQL query to retrieve all products
        SELECT * FROM products;
        """,

        """
        class Animal:
            def __init__(self, name):
                self.name = name

            def speak(self):
                pass
        """,
    ]

    code_pointers_list = [
        {
            'delta_code': {
                'file_path': 'path/to/changed/file1.txt',
                'change_type': 'Modified',
                'change_content': 'Updated function implementation.'
            },
            'text_description': 'Fixing a bug in the function.'
        },
        {
            'delta_code': {
                'file_path': 'path/to/changed/file2.txt',
                'change_type': 'Added',
                'change_content': 'New feature added.'
            },
            'text_description': 'Implementing a new feature.'
        },
        {
            'delta_code': {
                'file_path': 'path/to/changed/file3.py',
                'change_type': 'Modified',
                'change_content': 'Optimized code for better performance.'
            },
            'text_description': 'Code optimization.'
        },
        {
            'delta_code': {
                'file_path': 'path/to/changed/file4.java',
                'change_type': 'Modified',
                'change_content': 'Refactored the code for readability.'
            },
            'text_description': 'Refactoring code.'
        },
        {
            'delta_code': {
                'file_path': 'path/to/changed/file5.java',
                'change_type': 'Added',
                'change_content': 'Implemented a new class.'
            },
            'text_description': 'Adding a new class.'
        },
        {
            'delta_code': {
                'file_path': 'path/to/changed/file3.py',
                'change_type': 'Modified',
                'change_content': 'Optimized code for better performance.'
            },
            'text_description': 'Code optimization.'
        },
        {
            'delta_code': {
                'file_path': 'path/to/changed/file4.java',
                'change_type': 'Modified',
                'change_content': 'Refactored the code for readability.'
            },
            'text_description': 'Refactoring code.'
        },
        {
            'delta_code': {
                'file_path': 'path/to/changed/file5.java',
                'change_type': 'Added',
                'change_content': 'Implemented a new class.'
            },
            'text_description': 'Adding a new class.'
        },{
            'delta_code': {
                'file_path': 'path/to/changed/file6.py',
                'change_type': 'Modified',
                'change_content': 'Fixed a critical bug.'
            },
            'text_description': 'Bug fix.'
        },{
            'delta_code': {
                'file_path': 'path/to/changed/file7.py',
                'change_type': 'Added',
                'change_content': 'Added unit tests.'
            },
            'text_description': 'Adding unit tests.'
        },{
            'delta_code': {
                'file_path': 'path/to/changed/file8.js',
                'change_type': 'Modified',
                'change_content': 'Improved code readability.'
            },
            'text_description': 'Enhancing code readability.'
        },{
            'delta_code': {
                'file_path': 'path/to/changed/file9.py',
                'change_type': 'Added',
                'change_content': 'Implemented a new feature.'
            },
            'text_description': 'Adding a new feature.'
        },{
            'delta_code': {
                'file_path': 'path/to/changed/file10.java',
                'change_type': 'Modified',
                'change_content': 'Optimized database queries.'
            },
            'text_description': 'Database optimization.'
        },
    ]
