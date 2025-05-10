import pytest
import shutil

from pathlib import Path


@pytest.fixture(scope='session')
def base_dir(tmp_path_factory):
    base_path = tmp_path_factory.mktemp('root/')
    module_path = Path(base_path/'niagara'/'4.12/')
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