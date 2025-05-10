from pathlib import Path
import os
from niagara_repo.upload_handeling import store_module


def test_save_module_to_repo(tmp_module_dir):
    module_dir = tmp_module_dir
    assert module_dir.exists()

def test_module_repo_dir_exits(base_dir):
    base_dir = base_dir
    assert (base_dir/'niagara'/'4.12').exists()
    assert(base_dir/'uploads')

def test_store_module(base_dir, set_working_dir, tmp_module_dir):
    source_dir = tmp_module_dir
    target_dir = base_dir/'niagara'/'4.12'
    assert  (source_dir/'testModule.jar').exists()
    assert not (target_dir/'testModule.jar').exists()

    store_module('testModule.jar', target_dir)
    assert (target_dir/'testModule.jar').exists()
    assert (target_dir/'testModule.jar').is_file()

