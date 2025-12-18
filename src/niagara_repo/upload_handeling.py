import shutil
import subprocess

from pathlib import Path
from os import PathLike
from zipfile import ZipFile
import xml.etree.ElementTree as ET

ALLOWED_EXTENSIONS = 'jar'

def check_file_type(filename:str)->bool:
    """Checks the file type and confirms the file extention is approved type.

    Args:
        filename (str): Name of file with extention.

    Returns:
        bool: True if allowed extension.
    """    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def store_module(module_name: str, destination_dir: PathLike) -> None:
    base_path = Path()  
    module_path = base_path/'uploads'/module_name
    shutil.copy(module_path, destination_dir)

def test_get_module_info():
    base_dir = (Path(__file__).parent.parent.parent)
    file_path = base_dir/"tests/resources/modules/4.12"
    module_name = "vykonPro-doc.jar"
    return get_module_info(file_path, module_name)


def get_module_info(file_path: PathLike, module_name: str) -> dict[str, str]:
    """Parses the .jar files module.xml from the META-INF and return the meta data

    Args:
        file_path (PathLike): Path to module.
        module_name (str): name of module with extention.

    Returns:
        dict[str, str]: Module meta Data
    """
    file_path = Path(file_path)
    with ZipFile(file_path/module_name, 'r') as folder:
        file = folder.open("META-INF/module.xml", "r")
        tree =  ET.parse(file)
        root = tree.getroot()
        return root.attrib

def  verify_jar_signature(module_name: str) -> bool:
    """Calls Jarsigner tool to verify module signature

    Args:
        module_name (str): Name of the .jar module to be checked

    Returns:
        bool: Verification confirmation
    """
    output = subprocess.run(['jarsigner', '-verify', module_name], capture_output=True, text=True)

    if "jar verified." in output.stdout:
        jar_verication = True
        print('Pass')
    else:
        jar_verication = False
    return jar_verication


if __name__ == "__main__":
    print(test_get_module_info())


    # for element in root.iter('module'):
    #     print(element.attrib)
