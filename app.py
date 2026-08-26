from flask import Flask,request,jsonify
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

#filter books
#search a book
#add pagination
@app.get('/api/v1/books')
def get_books():
    #query parameters
    search=request.args.get("search")
    print("Search parameter: ",search)
    author=request.args.get("author")
    print("Author parameter: ",author)
    year=request.args.get("year")
    print("Year parameter: ",year)
    #pagination parameters
    page=request.args.get("page",default=1,type=int)
    print("Page parameter: ",page)
    per_page=request.args.get("per_page",default=5,type=int)
    print("per_page parameter: ",per_page)
    #validate pagination
    if page<1:
        return jsonify({
            "error":"Page must be greater than or equal to 1"
        }),400
    if per_page<1 or per_page>100:
        return jsonify({
            "error":"per_page must be between 1 and 100"
        }),400
    #start with all books
    filtered_books=books
    # print("Filtered books: ",filtered_books)
    #search by title
    if search:
        filtered_books=[
            book for book in filtered_books if search.lower() in book["title"].lower()
        ]
    #filter by author
    if author:
        filtered_books=[
            book for book in filtered_books if author.lower() in book["author"].lower()
        ]
    #filter by publication year
    if year is not None:
        try:
            year=int(year)
        except ValueError:
            return jsonify({
                "error":"Year must be an integer"
            }),400
        filtered_books=[
            book for book in filtered_books if book["year"]==year
        ]
    #total number of matching books
    total=len(filtered_books)
    print("Total: ",total)
    #pagination calculation
    start=(page-1)*per_page
    print("Start: ",start)
    end=start+per_page
    print("End: ",end)
    paginated_books=filtered_books[start:end]
    print("Paginated books: ",paginated_books)
    #return response
    return jsonify({
        "data":paginated_books,
        "pagination":{
            "page":page,
            "per_page":per_page,
            "total":total,
            "pages":(total+per_page-1)//per_page

        }
    }),200

   
    return book_list
#get specific book by its id
@app.get('/api/v1/books/<int:id>')
def get_book_by_id(id):
    for book in books:
        if book['id']==id:
          return book
    return {"message":"Book not found"},404
    
#create book
@app.post("/api/v1/books")
def create_book():
    data=request.get_json()
    new_book={
        "id":len(books)+1,
        "title":data["title"],
        "author":data["author"],
        "year":data["year"]
    }
    books.append(new_book)
    return new_book,201
#modify part of an existing data
@app.patch("/api/v1/books/<int:id>")
def update_book(id):
    data=request.get_json()
    for book in books:
        if book["id"]==id:
            if "title" in data:
                book["title"]=data["title"]
            if "author" in data:
                book["author"]=data["author"]
            if "year" in data:
                book["year"]=data["year"]
            return book
    return {"error":"Book not found"},404
#delete a book
@app.delete("/api/v1/books/<int:id>")
def delete_book(id):
    for book in books:
        if book['id']==id:
            books.remove(book)
            return "",204
    return {"error":"Book not found"},404
if __name__=="__main__":
    app.run(debug=True)