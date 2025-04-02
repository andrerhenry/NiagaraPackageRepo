import os
import json

def create_module_manifest():
    list_of_files = os.listdir(os.getcwd())


    manifest ={}
    n= 0
    #manifest["info"] = []
    for file in list_of_files:
        name = file.split('.')[0]
        extention = file.split('.')[-1]

        if extention == "txt":
            info = {"file": file, "extention": extention}
            manifest[name] = {"file": file, "extention": extention}


    with open("manifest.json", "w") as file:
        file.write(json.dumps(manifest))

    with open("manifest.json", "r") as file:
        data = json.loads(file.read())
        print(data["temp"]["file"])



if __name__ == "__main__":
    create_module_manifest()