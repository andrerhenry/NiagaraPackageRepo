import shutil


from pathlib import Path
from os import PathLike


def store_module(module_name: str, destination_dir: PathLike) -> None:
    base_path = Path()  
    module_path = base_path/'uploads'/base_path
    shutil.copy(module_path, destination_dir)