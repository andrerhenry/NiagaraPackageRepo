from pathlib import Path

def test_save_module_to_repo(tmp_module_dir):
    module_dir = tmp_module_dir
    assert module_dir.exists()

def test_module_repo_dir_exits(base_file_structure):
    base_dir = base_file_structure
    assert (base_dir/'naigara'/'4.12').exists()
    assert(base_dir/'uploads')

def test_module_stored_repo(base_file_structure, simuluate_upload):
    base_dir = base_file_structure
    source_dir = base_dir/'uploads'
    target_dir = base_dir/'naigara'/'4.12'
    assert  (source_dir/'vykonPro-rt.jar').exists()
    assert not (target_dir/'vykonPro-rt.jar').exists()
    # store_module()
    assert (target_dir/'vykonPro-rt.jar').exists()

    