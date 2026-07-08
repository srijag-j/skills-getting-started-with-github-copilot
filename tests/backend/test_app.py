from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_signup_updates_activity_participants():
    email = "signupstudent@mergington.edu"

    signup_response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert signup_response.status_code == 200

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    activity = activities_response.json()["Chess Club"]
    assert email in activity["participants"]


def test_student_can_be_removed_from_activity():
    email = "newstudent@mergington.edu"

    signup_response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert signup_response.status_code == 200

    remove_response = client.delete(f"/activities/Chess Club/signup?email={email}")
    assert remove_response.status_code == 200

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    activity = activities_response.json()["Chess Club"]
    assert email not in activity["participants"]
