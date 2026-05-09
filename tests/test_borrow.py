def test_borrow_book(test_client):

    response = test_client.post(
        "/borrow",
        json={
            "member_id": 1,
            "book_id": 1
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "message": "Book Borrowed"
    }

def test_return_book(test_client):

    response = test_client.put("/return/1")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Book Returned"
    }