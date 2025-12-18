from pathlib import Path
import os
import zipfile
from niagara_repo.upload_handeling import store_module, get_module_info, verify_jar_signature

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

def test_get_module_info_data_type():
    base_dir = (Path(__file__).parent)
    file_path = base_dir/'resources/modules/4.12'
    module_name = 'vykonPro-doc.jar'
    data = get_module_info(file_path, module_name)
    assert  isinstance(data, dict)

def test_get_module_info_data():
    base_dir = (Path(__file__).parent)
    file_path = base_dir/'resources/modules/4.12'
    module_name = 'vykonPro-doc.jar'
    data = get_module_info(file_path, module_name)
    assert data['name'] == 'vykonPro-doc'
    assert data['vendor']== 'VYKON'
    assert data['vendorVersion'] == "4.12.0.16" 

def test_verify_jar_signature(base_dir, set_working_dir, simuluate_upload):
    getting_path = base_dir
    module_path = getting_path/'uploads/vykonPro-doc.jar'
    assert verify_jar_signature(module_path) == True

