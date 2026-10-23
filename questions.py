# ==========================================
# TECHNICAL INTERVIEW QUESTIONS
# ==========================================

technical_questions = [

    {
        "question": "What is OOP?",
        "answer": "OOP stands for Object-Oriented Programming. It is a programming approach based on objects and classes. The main concepts are Encapsulation, Inheritance, Polymorphism and Abstraction."
    },

    {
        "question": "What is inheritance?",
        "answer": "Inheritance is an OOP concept where one class acquires the properties and methods of another class."
    },

    {
        "question": "What is an Operating System?",
        "answer": "An Operating System is system software that manages computer hardware and provides services to application programs."
    },

    {
        "question": "What is a Data Structure?",
        "answer": "A data structure is a way of organizing and storing data so that it can be accessed and modified efficiently."
    },

    {
        "question": "What is a database?",
        "answer": "A database is an organized collection of data that can be stored, accessed, managed and updated efficiently."
    },

    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted and general-purpose programming language known for its simple syntax and readability."
    },

    {
        "question": "What is an algorithm?",
        "answer": "An algorithm is a step-by-step procedure used to solve a problem or perform a task."
    },

    {
        "question": "What is a class?",
        "answer": "A class is a blueprint or template used to create objects."
    }
]


# ==========================================
# HR INTERVIEW QUESTIONS
# ==========================================

hr_questions = [

    {
        "question": "Tell me about yourself.",
        "answer": "Give a short introduction including your education, technical skills, projects, strengths and career goals."
    },

    {
        "question": "What are your strengths?",
        "answer": "Example: My strengths are quick learning, problem solving, teamwork and willingness to learn new technologies."
    },

    {
        "question": "What is your weakness?",
        "answer": "Mention a genuine but manageable weakness and explain what you are doing to improve it."
    },

    {
        "question": "Why should we hire you?",
        "answer": "You can explain how your technical skills, learning attitude, teamwork and willingness to contribute make you suitable for the position."
    },

    {
        "question": "How do you handle pressure?",
        "answer": "I handle pressure by prioritizing tasks, staying organized and focusing on solving one problem at a time."
    },

    {
        "question": "Where do you see yourself in five years?",
        "answer": "I see myself developing strong technical expertise, taking more responsibilities and contributing to meaningful projects."
    },

    {
        "question": "Why do you want this job?",
        "answer": "Explain your interest in the role, the skills you want to develop and how you can contribute to the organization."
    }
]


# ==========================================
# CODING INTERVIEW QUESTIONS
# ==========================================

coding_questions = [

    {
        "question": "Write a Python program to check whether a number is even or odd.",
        "answer": """num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")"""
    },

    {
        "question": "Write a Python program to find the largest of two numbers.",
        "answer": """a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
else:
    print(b)"""
    },

    {
        "question": "Write a Python program to reverse a string.",
        "answer": """text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed:", reverse)"""
    },

    {
        "question": "Write a Python program to calculate factorial of a number.",
        "answer": """num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)"""
    },

    {
        "question": "Write a Python program to check whether a number is prime.",
        "answer": """num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")"""
    }
]