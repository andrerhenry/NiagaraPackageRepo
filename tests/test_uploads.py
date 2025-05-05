from pathlib import Path

def test_save_module_to_repo(tmp_module_dir):
    module_dir = tmp_module_dir
    assert module_dir.exists()

def test_module_repo_dir_exits(make_tmp_file_structure):
    base_dir = make_tmp_file_structure
    assert (base_dir/'naigara'/'4.12').exists()