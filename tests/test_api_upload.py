

from requests import request
from pathlib import Path


def test_api_upload_test_file(setup_test_server, base_dir, set_working_dir):
    client = setup_test_server

    with open('test_file.txt', 'wb+') as file:
        file.write(b'testing text in file.')
        data = {'file': (file, 'test_file.txt')}  # client expects post in diffrent form from requests module
        response = client.post('/api/uploads', data = data)

    saved_file_location = Path(base_dir/'uploads'/'test_file.txt')

    assert response.status_code == 200
    assert saved_file_location.exists()
    (Path('test_file.txt').unlink())



def test_ping(setup_test_server):
    client = setup_test_server
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.get_json() == {"message": "pong"}