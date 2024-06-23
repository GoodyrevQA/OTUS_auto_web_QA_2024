import json
from csv import DictReader
from files import BOOKS_FILE_PATH, USERS_FILE_PATH

users_with_books = []

with open(USERS_FILE_PATH, "r", encoding="utf-8") as fj:
    users = json.load(fj)

for user in users:
    users_with_books.append(
        {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [],
        }
    )

with open(BOOKS_FILE_PATH, newline="") as fc:
    books = DictReader(fc)
    counter = 0
    for book in books:
        users_with_books[counter % len(users_with_books)]["books"].append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"],
            }
        )
        counter += 1

with open("result.json", "w") as f:
    json.dump(users_with_books, f, indent=4)
