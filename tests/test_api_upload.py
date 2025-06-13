

from requests import request
from pathlib import Path
import os
import requests

def test_api_saves_upload(setup_test_server, base_dir, set_working_dir):

    client = setup_test_server


    with open('temp.txt', 'wb+') as file:
        file.write(b'testing text in file.')
        data = {'file': (file, 'temp.txt')}  # 'file' is the field name expected by the server 
        # data = request('POST', 'http://127.0.0.1:5000/api/uploads', files=files)
        data = client.post('/api/uploads', data = data)

    print(data.content_length)
    
    print('form client post:', data.status_code)

    saved_file_location = Path(base_dir/'uploads'/'test_file.txt')


    # print('\n\ncurrent working directory:', os.getcwd())
    # print('list dir:', os.listdir(), os.listdir('niagara'))
    # print('upload file:', Path('test_file.txt').exists())
    # print('uploaded file as save location:',saved_file_location.exists())
    # print('\n\n')

    assert data.status_code == 200
    assert saved_file_location.exists()
    (Path('test_file.txt').unlink())



def test_ping(setup_test_server):
    client = setup_test_server
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.get_json() == {"message": "pong"}