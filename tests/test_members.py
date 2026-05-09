def test_create_member(test_client):

    response = test_client.post(
        "/members",
        json={
            "name": "Rahul",
            "email": "rahul@test.com",
            "course": "BCA"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data


def test_get_members(test_client):

    response = test_client.get("/members")

    assert response.status_code == 200


def test_update_member(test_client):

    # Create member
    create_response = test_client.post(
        "/members",
        json={
            "name": "Rahul",
            "email": "rahul_update@test.com",
            "course": "BCA"
        }
    )

    member_id = create_response.json()["id"]

    # Update member
    response = test_client.put(
        f"/members/{member_id}",
        json={
            "name": "Updated Rahul",
            "email": "updated@test.com",
            "course": "MCA"
        }
    )

    assert response.status_code == 200


def test_delete_member(test_client):

    # Create member
    create_response = test_client.post(
        "/members",
        json={
            "name": "Delete User",
            "email": "delete@test.com",
            "course": "BCA"
        }
    )

    member_id = create_response.json()["id"]

    # Delete member
    response = test_client.delete(
        f"/members/{member_id}"
    )

    assert response.status_code == 200