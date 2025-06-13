import pytest
import shutil

from flask import Flask, jsonify
from pathlib import Path

from niagara_repo.main import setup_app

@pytest.fixture(scope='session')
def setup_test_server(base_dir):
    ALLOWED_EXTENSIONS = {'jar', 'txt'} # Allow Test files for testing 

    app = setup_app()
    # Override configuration for testing
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = base_dir/'uploads'


    # Check test server is working
    @app.route("/ping")
    def ping():
        return jsonify({"message": "pong"})


    # Move this to own resource?
    #from niagara_repo.main import upload_file
    app.test_client()
    with app.test_client() as client:
        yield client




@pytest.fixture(scope='session')
def base_dir(tmp_path_factory):
    base_path = tmp_path_factory.mktemp('root')
    module_path = Path(base_path/'niagara'/'4.12')
    module_path.mkdir(parents=True)

    uploads_dirs = Path(base_path/'uploads/')
    uploads_dirs.mkdir(parents=True)
    return Path(base_path)

@pytest.fixture
def simuluate_upload(base_dir):
    base_path = base_dir
    module_path = Path(__file__).parent/'resources/modules/4.12'
    
    shutil.copytree(module_path, base_path/'uploads', dirs_exist_ok=True)

@pytest.fixture
def set_working_dir(base_dir, monkeypatch):
    monkeypatch.chdir(base_dir)


@pytest.fixture
def tmp_module_dir(base_dir):
    CONTENT = 'A temporary module for testing its placement.'
    module_dir = Path(base_dir/'uploads')
    module_dir.mkdir(parents=True, exist_ok=True)
    
    module_path = module_dir/'testModule.jar'
    module_path.write_text(CONTENT, encoding='utf-8')
    return module_dir

@pytest.fixture
def set_directory_modules_4_12(tmp_path, monkeypatch):
    new_path = tmp_path/'4.12'
    monkeypatch.chdir(new_path)
    return new_path