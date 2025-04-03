import os
import json

def create_module_manifest():
    list_of_files = os.listdir(os.getcwd())
    
    
    manifest ={}
    for file in list_of_files:
        extension = file.split('.')[-1]
        module_profile = (file.split('.')[0]).split('-')[-1]
        name = (file.split('.')[0]).split('-')[0]

        if extension == "jar":
            if name not in manifest:
                manifest[name] = {"file": [file], "profile": [module_profile]}
            elif name in manifest.keys():
                manifest[name]["file"].append(file)
                manifest[name]["profile"].append(module_profile)
                



    with open("manifest.json", "w") as file:
        manifest = dict(sorted(manifest.items()))
        file.write(json.dumps(manifest))


def read_module_manifest():
    with open("manifest.json", "r") as file:
        data = json.loads(file.read())
        print(data["temp"]["file"])



if __name__ == "__main__":
    create_module_manifest()