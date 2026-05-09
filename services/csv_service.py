import pandas as pd
from sqlalchemy.orm import Session
from book import Book

def upload_books(file_path, db: Session):

    # Read CSV as strings
    df = pd.read_csv(file_path, dtype=str)

    print(df.columns)

    for _, row in df.iterrows():

        isbn = str(row['ISBN']).strip()

        # Duplicate check
        existing = db.query(Book).filter(
            Book.isbn == isbn
        ).first()

        if existing:
            continue

        book = Book(
            title=str(row['Title']).strip(),
            author=str(row['Author']).strip(),
            isbn=isbn,
            category=str(row['Category']).strip(),
            quantity=int(row['Quantity']),
            available_quantity=int(row['Quantity'])
        )

        db.add(book)

    db.commit()

    print("Books uploaded successfully")