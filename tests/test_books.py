def test_add_book(test_client):

    response = test_client.post(
        "/books",
        json={
            "title": "Python",
            "author": "Naina",
            "isbn": "9999",
            "category": "Programming",
            "quantity": 10
        }
    )

    assert response.status_code == 200


def test_get_books(test_client):

    response = test_client.get("/books")

    assert response.status_code == 200


def test_update_book(test_client):

    # First create book
    test_client.post(
        "/books",
        json={
            "title": "Python",
            "author": "Naina",
            "isbn": "8888",
            "category": "Programming",
            "quantity": 10
        }
    )

    response = test_client.put(
        "/books/1",
        json={
            "title": "Updated Python",
            "author": "Naina",
            "isbn": "8888",
            "category": "Programming",
            "quantity": 20
        }
    )

    assert response.status_code == 200


def test_delete_book(test_client):

    # First create book
    test_client.post(
        "/books",
        json={
            "title": "Delete Book",
            "author": "Naina",
            "isbn": "7777",
            "category": "Programming",
            "quantity": 5
        }
    )

    response = test_client.delete("/books/1")

    assert response.status_code == 200