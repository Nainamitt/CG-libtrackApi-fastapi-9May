def test_borrow_book(test_client):

    # Create member
    member_response = test_client.post(
        "/members",
        json={
            "name": "Rahul",
            "email": "rahul@test.com",
            "course": "BCA"
        }
    )

    member_id = member_response.json()["id"]

    # Create book
    book_response = test_client.post(
        "/books",
        json={
            "title": "Python",
            "author": "Naina",
            "isbn": "1111",
            "category": "Programming",
            "quantity": 5
        }
    )

    book_id = book_response.json()["id"]

    # Borrow
    response = test_client.post(
        "/borrow",
        json={
            "member_id": member_id,
            "book_id": book_id
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "borrow_id" in data


def test_return_book(test_client):

    # Create member
    member_response = test_client.post(
        "/members",
        json={
            "name": "Rahul",
            "email": "rahul2@test.com",
            "course": "BCA"
        }
    )

    member_id = member_response.json()["id"]

    # Create book
    book_response = test_client.post(
        "/books",
        json={
            "title": "FastAPI",
            "author": "Naina",
            "isbn": "2222",
            "category": "Programming",
            "quantity": 5
        }
    )

    book_id = book_response.json()["id"]

    # Borrow
    borrow_response = test_client.post(
        "/borrow",
        json={
            "member_id": member_id,
            "book_id": book_id
        }
    )

    borrow_id = borrow_response.json()["borrow_id"]

    # Return
    response = test_client.put(
        f"/return/{borrow_id}"
    )

    assert response.status_code == 200