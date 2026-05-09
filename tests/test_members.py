def test_add_member(test_client):

    response = test_client.post(
        "/members",
        json={
            "name": "Rahul",
            "email": "rahul@test.com",
            "course": "BTech"
        }
    )

    assert response.status_code == 200

def test_get_members(test_client):

    response = test_client.get("/members")

    assert response.status_code == 200

def test_update_member(test_client):

    response = test_client.put(
        "/members/1",
        json={
            "name": "Updated Rahul",
            "email": "updated@test.com",
            "course": "MCA"
        }
    )

    assert response.status_code == 200

def test_delete_member(test_client):

    response = test_client.delete("/members/1")

    assert response.status_code == 200