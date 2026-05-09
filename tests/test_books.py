def test_create_book(test_client):

    response = test_client.post(
        "/books",
        json={
            "title": "Python Basics",
            "author": "Naina",
            "isbn": "1111",
            "category": "Programming",
            "quantity": 5
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data


def test_get_books(test_client):

    response = test_client.get("/books")

    assert response.status_code == 200


def test_update_book(test_client):

    # Create book
    create_response = test_client.post(
        "/books",
        json={
            "title": "Old Book",
            "author": "Author",
            "isbn": "2222",
            "category": "Programming",
            "quantity": 5
        }
    )

    book_id = create_response.json()["id"]

    # Update
    response = test_client.put(
        f"/books/{book_id}",
        json={
            "title": "Updated Book",
            "author": "Updated Author",
            "isbn": "3333",
            "category": "Technology",
            "quantity": 10
        }
    )

    assert response.status_code == 200


def test_delete_book(test_client):

    # Create book
    create_response = test_client.post(
        "/books",
        json={
            "title": "Delete Book",
            "author": "Author",
            "isbn": "4444",
            "category": "Programming",
            "quantity": 5
        }
    )

    book_id = create_response.json()["id"]

    # Delete
    response = test_client.delete(
        f"/books/{book_id}"
    )

    assert response.status_code == 200