import requests
import pytest
url = 'http://localhost:5000/tasks'


def test_01_authorization_user():
    response = requests.put('http://localhost:5000/user',
                            json={"username": 'test'})
    assert response.status_code == 200


def test_02_add_task():
    response = requests.post(url, json={"date": {"day": 3,
                                                 "month": 1,
                                                 "year": 2020},
                                        "task": "go to the cafe"})
    assert response.status_code == 201\
        and response.json() == {"day": 3,
                                "month": 1,
                                "year": 2020,
                                "task": "go to the cafe",
                                "id": 1}


def test_03_get_all_tasks():
    response = requests.get(url)
    assert response.status_code == 200\
        and response.json() == [{"day": 3,
                                 "month": 1,
                                 "year": 2020,
                                 "task": "go to the cafe",
                                 "id": 1}]


def test_04_change_task_with_id():
    response = requests.put('http://localhost:5000/tasks/1',
                            json={"task": "go to the home"})
    assert response.status_code == 200 \
        and response.json() == {"day": 3,
                                "month": 1,
                                "year": 2020,
                                "task": "go to the home",
                                "id": 1}


def test_05_get_task_with_id():
    response = requests.get('http://localhost:5000/tasks/1')
    assert response.status_code == 200 \
        and response.json() == {"day": 3,
                                "month": 1,
                                "year": 2020,
                                "task": "go to the home",
                                "id": 1}


def test_06_get_tasks_from_date():
    response = requests.get('http://localhost:5000/tasks/actions',
                            params={"day": 3, "month": 1, "year": 2020})
    assert response.status_code == 200 \
        and response.json() == [{"day": 3,
                                 "month": 1,
                                 "year": 2020,
                                 "task": "go to the home",
                                 "id": 1}]


def test_07_get_tasks_from_period():
    response = requests.post('http://localhost:5000/tasks/actions',
                             json={"from": {"day": 1,
                                            "month": 1,
                                            "year": 2020},
                                   "to": {"day": 1,
                                          "month": 1,
                                          "year": 2021}})
    assert response.status_code == 200 \
        and response.json() == [{"day": 3,
                                 "month": 1,
                                 "year": 2020,
                                 "task": "go to the home",
                                 "id": 1}]


def test_08_delete_task_with_id():
    response = requests.delete('http://localhost:5000/tasks/1')
    assert response.status_code == 200 \
        and response.json() == {"day": 3,
                                "month": 1,
                                "year": 2020,
                                "task": "go to the home",
                                "id": 1}


def test_09_get_current_user():
    response = requests.get('http://localhost:5000/user')
    assert response.status_code == 200 \
        and response.json() == {"username": 'test'}


def test_10_add_new_user():
    response = requests.post('http://localhost:5000/user',
                             json={"username": "test"})
    assert response.status_code == 400


if __name__ == "__main__":
    pytest.main()
