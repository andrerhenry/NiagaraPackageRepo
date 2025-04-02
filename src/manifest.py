import os
import json

def create_module_manifest():
    list_of_files = os.listdir(os.getcwd())


    manifest ={}
    #manifest["info"] = []
    for file in list_of_files:
        name = file.split('.')[0]
        extention = file.split('.')[-1]

        if extention == "txt":
            info = {"file": file, "extention": extention}
            manifest[name] = {"file": file, "extention": extention}
            print(manifest)

    with open("manifest.json", "w") as file:
        file.write(json.dumps(manifest))
        print(type(json.dumps(manifest)))

    with open("manifest.json", "r") as file:

        data = json.loads(file.read())
        print(type(data))
        print(data)



if __name__ == "__main__":
    create_module_manifest()