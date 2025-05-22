import shutil


from pathlib import Path
from os import PathLike
from zipfile import ZipFile
import xml.etree.ElementTree as ET


def store_module(module_name: str, destination_dir: PathLike) -> None:
    base_path = Path()  
    module_path = base_path/'uploads'/module_name
    shutil.copy(module_path, destination_dir)

def get_module_info():
    base_dir = (Path(__file__).parent.parent.parent)
    file_path = base_dir/"tests/resources/modules/4.12"
    with ZipFile(file_path/"vykonPro-doc.jar", 'r') as folder:
        file = folder.open("META-INF/module.xml", "r")
        return ET.parse(file)

def parse_xml_data():
    ET.parse()

if __name__ == "__main__":
    tree =  get_module_info()
    root = tree.getroot()
    print(root)
    print(root.attrib)


    # for element in root.iter('module'):
    #     print(element.attrib)
