from flask import Flask
app=Flask(__name__)
books = [
    {
        "id": 1,
        "title": "The Silent Algorithm",
        "author": "Daniel Carter",
        "year": 2018
    },
    {
        "id": 2,
        "title": "Python for Everyone",
        "author": "Maya Brooks",
        "year": 2020
    },
    {
        "id": 3,
        "title": "The Last Network",
        "author": "James Wilson",
        "year": 2017
    },
    {
        "id": 4,
        "title": "Building Better APIs",
        "author": "Sarah Mitchell",
        "year": 2022
    },
    {
        "id": 5,
        "title": "Linux from the Ground Up",
        "author": "Michael Adams",
        "year": 2019
    },
    {
        "id": 6,
        "title": "The Digital Fortress",
        "author": "Nathan Reed",
        "year": 2016
    },
    {
        "id": 7,
        "title": "Mastering HTTP",
        "author": "Olivia Parker",
        "year": 2021
    },
    {
        "id": 8,
        "title": "Database Design Essentials",
        "author": "Robert Hayes",
        "year": 2018
    },
    {
        "id": 9,
        "title": "Practical Flask Development",
        "author": "Emma Collins",
        "year": 2023
    },
    {
        "id": 10,
        "title": "Secure Web Applications",
        "author": "David Morgan",
        "year": 2020
    },
    {
        "id": 11,
        "title": "The Code Breaker",
        "author": "Lucas Bennett",
        "year": 2015
    },
    {
        "id": 12,
        "title": "Modern Python Patterns",
        "author": "Sophia Turner",
        "year": 2024
    },
    {
        "id": 13,
        "title": "Understanding REST",
        "author": "Ethan Cooper",
        "year": 2019
    },
    {
        "id": 14,
        "title": "Inside the Operating System",
        "author": "Grace Morgan",
        "year": 2017
    },
    {
        "id": 15,
        "title": "API Security Fundamentals",
        "author": "Daniel Brooks",
        "year": 2022
    },
    {
        "id": 16,
        "title": "Docker for Developers",
        "author": "Ryan Foster",
        "year": 2021
    },
    {
        "id": 17,
        "title": "The Cloud Architect",
        "author": "Jessica Adams",
        "year": 2023
    },
    {
        "id": 18,
        "title": "Programming with Python",
        "author": "Andrew Mitchell",
        "year": 2018
    },
    {
        "id": 19,
        "title": "Web Security in Practice",
        "author": "Samuel Carter",
        "year": 2020
    },
    {
        "id": 20,
        "title": "Engineering Reliable APIs",
        "author": "Laura Wilson",
        "year": 2025
    }
]
# print(books)
@app.route('/')
def hello():
    return 'Hello,from Flask'
if __name__=="__main__":
    app.run(debug=True)