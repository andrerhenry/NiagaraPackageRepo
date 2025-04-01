import os
import json

def create_module_manifest():
    list_of_files = os.listdir(os.getcwd())
    print(type(list_of_files))
    print(type(list_of_files[0]))

    manifest ={}
    for file in list_of_files:
        name = file.split('.')[0]
        extention = file.split('.')[-1]
        print(extention)

        if extention == "txt":
            manifest.update({name: file})
    print(manifest["temp"])

    with open("manifest.json", "w") as file:
        file.write(json.dumps(manifest))


if __name__ == "__main__":
    create_module_manifest()