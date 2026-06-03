# Task-3-Sarth-patel
# Book Recommendation System

## Introduction

Choosing a good book can sometimes be difficult because there are thousands of books available in different genres. The purpose of this project is to help users find books according to their interests.

The Book Recommendation System is a simple Python-based application that recommends books based on the genre selected by the user. It uses a basic recommendation technique where books are filtered according to the user's preference and then displayed in order of their ratings.


## Project Objective

The main objective of this project is:

- To recommend books based on user interests.
- To understand the basic concept of recommendation systems.
- To implement filtering and sorting using Python.
- To provide a simple and user-friendly recommendation experience.


## Tools and Technologies Used

- Python 3
- Pandas Library
- CSV File for Dataset
- VS Code / PyCharm (Optional)


## Dataset Information

The dataset contains information about different books, including:

- Book Title
- Author Name
- Genre
- Rating

The dataset covers multiple genres such as:

- Fantasy
- Mystery
- Science Fiction
- Romance
- Self Help
- Biography
- History
- Fiction
- Technology
- Motivation


## How the System Works

The recommendation process is very simple:

1. The program loads the dataset.
2. All available genres are displayed to the user.
3. The user selects a genre.
4. The system searches for books belonging to that genre.
5. Books are sorted according to their ratings.
6. The recommended books are displayed.

This approach is known as **Content-Based Recommendation**, where recommendations are made using the user's interests.


## Algorithm

1. Start the program.
2. Load the book dataset from the CSV file.
3. Display available genres.
4. Take user input.
5. Filter books based on the selected genre.
6. Sort books according to ratings.
7. Display recommendations.
8. Ask the user whether they want another recommendation.
9. End the program.


## How to Run the Project

### Install Required Library

```bash
pip install pandas
```

### Run the Program

For Windows:

```bash
python book_recommendation.py
```

For Mac/Linux:

```bash
python3 book_recommendation.py
```

---

## Sample Output


--------------------------
BOOK RECOMMENDATION SYSTEM
--------------------------

Available Genres:

1. Fantasy
2. Mystery
3. Romance
4. Technology

Select Genre Number: 1

Recommended Books:

Harry Potter
Author: J.K. Rowling
Rating: 4.9

The Hobbit
Author: J.R.R. Tolkien
Rating: 4.8


## Features

- Easy to use
- Genre-based recommendations
- Rating-based sorting
- Interactive menu
- Beginner-friendly implementation


## Conclusion

This project successfully recommends books based on user preferences. It provides a basic understanding of how recommendation systems work and how user interests can be used to generate useful suggestions. The project can be further improved by integrating machine learning techniques and advanced recommendation methods.


## Developed By

Sarth Patel

